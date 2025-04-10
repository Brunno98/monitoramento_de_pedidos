from application.dto.pedido_event_dto import PedidoEventDTO
from domain.value_objects.domain_date import DomainDate
from domain.value_objects.pedido_id import PedidoId
from aws_lambda_typing import events


class DynamoDBEventMapper:
    @staticmethod
    def to_pedido_event_dto(record: events.dynamodb_stream.DynamodbRecord, event_name: str) -> PedidoEventDTO:
        try:
            raw = record['dynamodb']['NewImage']
            record_date = record['dynamodb']['ApproximateCreationDateTime']
            return PedidoEventDTO(
                pedido_id=PedidoId(raw['pedido_id']['S']),
                acao=event_name,
                status=raw['status']['S'],
                event_date=DomainDate.from_timestamp(record_date)
            )
        except KeyError as e:
            raise ValueError(f"Erro ao converter evento: campo ausente {e}")
        except Exception as e:
            raise ValueError(f"Erro inesperado no mapeamento do evento: {e}")
