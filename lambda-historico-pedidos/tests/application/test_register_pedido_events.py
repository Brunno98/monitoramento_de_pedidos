

import pytest
from application.dto.pedido_event_dto import PedidoEventDTO
from application.use_cases.register_pedido_events import RegisterPedidoEvent
from domain.entities.pedido import Pedido
from domain.repositories.pedido_event_repository import PedidoEventRepository
from domain.value_objects.domain_date import DomainDate
from domain.value_objects.pedido_id import PedidoId


@pytest.fixture
def pedido_event_repository():
    return DummyPedidoEventRepository()


@pytest.fixture
def use_case(pedido_event_repository):
    return RegisterPedidoEvent(pedido_event_repository)


def test_given_a_valid_pedido_event_dto__when_calls_register_pedido_use_case__should_register_it(
        use_case, pedido_event_repository):
    # given
    expected_pedido_id = PedidoId.generate()
    expected_acao = "INSERT"
    expected_status = "pendente"
    expected_event_date = DomainDate.now()
    pedido_dto = PedidoEventDTO(
        expected_pedido_id, expected_acao, expected_status, expected_event_date
    )
    assert not pedido_event_repository.contains(expected_pedido_id)

    # when
    use_case.execute(pedido_dto)

    # then
    assert pedido_event_repository.contains(expected_pedido_id)


class DummyPedidoEventRepository(PedidoEventRepository):

    def __init__(self):
        super().__init__()
        self.__pedidos = set()

    def register(self, pedido: Pedido) -> bool:
        self.__pedidos.add(pedido)
        return True

    def contains(self, pedido_id: PedidoId) -> bool:
        return bool(list(filter(lambda item: item.pedido_id == pedido_id, self.__pedidos)))
