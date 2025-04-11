

from application.dto.pedido_event_dto import PedidoEventDTO
from domain.repositories.pedido_event_repository import PedidoEventRepository


class RegisterLotePedidoEvents:

    def __init__(self, pedidoEventRepository: PedidoEventRepository):
        if not pedidoEventRepository:
            raise ValueError("'pedidoEventRepository' cannot be None")
        self.__pedidoEventRepository = pedidoEventRepository

    def execute(self, pedido_events: list[PedidoEventDTO]):
        pedidos = [pedido.to_domain() for pedido in pedido_events]

        self.__pedidoEventRepository.register_in_batch(pedidos)
