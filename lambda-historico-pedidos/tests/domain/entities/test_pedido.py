

from uuid import uuid4
from domain.entities.pedido import Pedido
from domain.value_objects.domain_date import DomainDate
from domain.value_objects.pedido_id import PedidoId


def test_given_valid_data__when_create_pedido__should_create_it():
    # given
    expected_pedido_id = PedidoId(str(uuid4()))
    expected_domain_date = DomainDate.now()
    expected_acao = "INSERT"
    expected_status = "pendente"

    # when
    pedido = Pedido(expected_pedido_id, expected_acao,
                    expected_status, expected_domain_date)

    # then
    assert pedido.pedido_id == expected_pedido_id
    assert pedido.event_date == expected_domain_date
    assert pedido.acao == expected_acao
    assert pedido.status == expected_status
