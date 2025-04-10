from application.dto.pedido_event_dto import PedidoEventDTO
from application.use_cases.register_pedido_events import RegisterPedidoEvent
from domain.value_objects.domain_date import DomainDate
from domain.value_objects.pedido_id import PedidoId
from infrastructure.repositories.pedido_event_respository_postgres import PedidoEventRepositoryPostgres


def main():
    repo = PedidoEventRepositoryPostgres()
    use_case = RegisterPedidoEvent(repo)

    pedido_id = PedidoId.generate()
    domain_date = DomainDate.now()
    acao = "INSERT"
    status = "pendente"

    input_dto = PedidoEventDTO(pedido_id, acao, status, domain_date)

    output = use_case.execute(input_dto)

    print(f"Event de pedido registrado! saída: {str(output)}")


if __name__ == "__main__":
    main()
