

from domain.entities.pedido import Pedido
from domain.repositories.pedido_event_repository import PedidoEventRepository
from infrastructure.db.connection import get_connection


class PedidoEventRepositoryPostgres(PedidoEventRepository):

    def register(self, pedido: Pedido) -> bool:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                            INSERT INTO historico_pedidos ("pedido_id", "acao", "status", "data_evento")
                            values (%s, %s, %s, %s);""",
                            (
                                pedido.pedido_id.getValue(),
                                pedido.acao,
                                pedido.status,
                                pedido.event_date.value
                            ))
        return True

    def register_in_batch(self, pedidos: list[Pedido]):
        values = [
            (
                pedido.pedido_id.getValue(),
                pedido.acao,
                pedido.status,
                pedido.event_date.value
            ) for pedido in pedidos
        ]

        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.executemany("""
                            INSERT INTO historico_pedidos ("pedido_id", "acao", "status", "data_evento")
                            values (%s, %s, %s, %s);""", values)
                conn.commit()
