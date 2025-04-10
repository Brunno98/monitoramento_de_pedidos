

from dataclasses import dataclass
from domain.value_objects.pedido_id import PedidoId


@dataclass(frozen=True)
class RegisteredPedidoEventDTO:
    pedido_id: PedidoId
    success: bool
