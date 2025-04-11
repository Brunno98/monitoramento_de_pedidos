

import json
import time
from application.use_cases.register_lote_pedido_events import RegisterLotePedidoEvents
from infrastructure.repositories.stream_info_repository import save_stream_info
from interfaces.aws.mappers.dynamodb_event_mapper import DynamoDBEventMapper
# from application.use_cases.register_pedido_events import RegisterPedidoEvent
from infrastructure.repositories.pedido_event_respository_postgres import PedidoEventRepositoryPostgres
from aws_lambda_typing import events, context


repo = PedidoEventRepositoryPostgres()
use_case = RegisterLotePedidoEvents(repo)


def lambda_handler(event: events.DynamoDBStreamEvent, context: context.Context):
    start = time.perf_counter()
    records = event.get('Records')

    dtos = []
    for record in records:
        event_name = record.get('eventName')
        if event_name == "REMOVE":
            print("Ignorando evento de remoção")
            continue
        try:
            dtos.append(DynamoDBEventMapper.to_pedido_event_dto(
                record, event_name))
        except Exception as e:
            print(
                f"❌ erro do ao converter dado para dto: {json.dumps(record)}.\n{e}")

    try:
        use_case.execute(dtos)
    except Exception as e:
        print(
            f"❌ erro ao realizar registro dos eventos: {json.dumps(records)}.\n{e}")
    response = {}

    end = time.perf_counter()
    elapsed = end - start
    save_stream_info(context.aws_request_id, len(records), elapsed)
    return response


# def lambda_handler(event: events.DynamoDBStreamEvent, context: context.Context):
#     start = time.perf_counter()
#     records = event.get('Records')

#     response = {}

#     for record in records:
#         event_name = record.get('eventName')
#         if event_name == "REMOVE":
#             print("Ignorando evento de remoção")
#             continue
#         try:
#             dto = DynamoDBEventMapper.to_pedido_event_dto(record, event_name)

#             result = use_case.execute(dto)

#             response[result.pedido_id.getValue()] = result.success
#             print("✅ sucesso!")
#         except Exception as e:
#             print(f"❌ erro do record: {json.dumps(record)}.\n{e}")

#     end = time.perf_counter()
#     elapsed = end - start
#     save_stream_info(context.aws_request_id, len(records), elapsed)
#     return response
