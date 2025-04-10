

from abc import ABC, abstractmethod

from domain.entities.pedido import Pedido


class PedidoEventRepository(ABC):

    @abstractmethod
    def register(pedido: Pedido) -> bool:
        pass
