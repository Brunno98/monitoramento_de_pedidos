

from domain.value_objects.domain_date import DomainDate
from domain.value_objects.pedido_id import PedidoId


class Pedido:
    pedido_id: PedidoId
    acao: str
    status: str
    event_date: DomainDate

    def __init__(self, pedido_id: PedidoId, acao: str, status: str, event_date: DomainDate):
        self.pedido_id = pedido_id
        self.acao = acao
        self.status = status
        self.event_date = event_date
