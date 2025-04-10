

from application.dto.pedido_event_dto import PedidoEventDTO
from application.dto.registered_pedido_event_dto import RegisteredPedidoEventDTO
from domain.repositories.pedido_event_repository import PedidoEventRepository


class RegisterPedidoEvent:

    def __init__(self, pedidoEventRepository: PedidoEventRepository):
        if not pedidoEventRepository:
            raise ValueError("'pedidoEventRepository' cannot be None")
        self.__pedidoEventRepository = pedidoEventRepository

    def execute(self, pedido_event: PedidoEventDTO) -> RegisteredPedidoEventDTO:
        pedido = pedido_event.to_domain()

        success = self.__pedidoEventRepository.register(pedido)

        return RegisteredPedidoEventDTO(pedido.pedido_id, success)
