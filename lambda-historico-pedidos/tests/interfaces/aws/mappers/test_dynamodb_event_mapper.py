from interfaces.aws.mappers.dynamodb_event_mapper import DynamoDBEventMapper
from application.dto.pedido_event_dto import PedidoEventDTO
from domain.value_objects.pedido_id import PedidoId
from domain.value_objects.domain_date import DomainDate
from aws_lambda_typing import events


def test_to_pedido_event_dto_should_map_dynamodb_record_correctly():
    # Arrange
    dynamodb_record: events.dynamodb_stream.DynamodbRecord = {
        "dynamodb": {
            "NewImage": {
                "pedido_id": {"S": "12345"},
                "status": {"S": "CRIADO"},
                "data_criacao": {"S": "2025-04-10T13:45:00"}
            },
            "ApproximateCreationDateTime": 1744326680
        }
    }

    # Act
    dto = DynamoDBEventMapper.to_pedido_event_dto(dynamodb_record, "INSERT")

    # Assert
    assert isinstance(dto, PedidoEventDTO)
    assert dto.pedido_id == PedidoId("12345")
    assert dto.acao == "INSERT"
    assert dto.status == "CRIADO"
    assert isinstance(dto.event_date, DomainDate)
    assert dto.event_date == DomainDate.from_str("2025-04-10T23:11:20")
