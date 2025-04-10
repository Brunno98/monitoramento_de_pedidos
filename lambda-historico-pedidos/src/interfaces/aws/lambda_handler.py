

import json
from interfaces.aws.mappers.dynamodb_event_mapper import DynamoDBEventMapper
from application.use_cases.register_pedido_events import RegisterPedidoEvent
from infrastructure.repositories.pedido_event_respository_postgres import PedidoEventRepositoryPostgres
from aws_lambda_typing import events


repo = PedidoEventRepositoryPostgres()
use_case = RegisterPedidoEvent(repo)


def lambda_handler(event: events.DynamoDBStreamEvent, context):
    records = event.get('Records')

    response = {}

    for record in records:
        event_name = record.get('eventName')
        if event_name == "REMOVE":
            print("Ignorando evento de remoção")
            continue
        try:
            dto = DynamoDBEventMapper.to_pedido_event_dto(record, event_name)

            result = use_case.execute(dto)

            response[result.pedido_id.getValue()] = result.success
            print("✅ sucesso!")
        except Exception as e:
            print(f"❌ erro do record: {json.dumps(record)}.\n{e}")

    return response
