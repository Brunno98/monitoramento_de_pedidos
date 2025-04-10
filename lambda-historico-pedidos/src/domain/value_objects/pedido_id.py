from uuid import uuid4
from domain.error.invalid_pedido_id import InvalidPedidoId

MAX_LENGTH = 36


class PedidoId:
    __value: str

    def __init__(self, value: str):
        if not value or len(value) == 0:
            raise InvalidPedidoId("id do pedido não pode ser vazio")
        if len(value) > MAX_LENGTH:
            raise InvalidPedidoId(
                f"id de pedido '{value}' é maior que o limite de {MAX_LENGTH} esperado")
        self.__value = value

    @classmethod
    def generate(cls) -> 'PedidoId':
        return PedidoId(str(uuid4()))

    def getValue(self) -> str:
        return self.__value
