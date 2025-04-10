
from dataclasses import dataclass

from domain.entities.pedido import Pedido
from domain.value_objects.domain_date import DomainDate
from domain.value_objects.pedido_id import PedidoId


@dataclass(frozen=True)
class PedidoEventDTO:
    pedido_id: PedidoId
    acao: str
    status: str
    event_date: DomainDate

    def to_domain(self) -> Pedido:
        return Pedido(
            self.pedido_id,
            self.acao,
            self.status,
            self.event_date
        )
