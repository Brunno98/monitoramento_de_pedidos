

CREATE TABLE historico_pedidos (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    pedido_id char(36) NOT NULL,
    acao varchar(50) NOT NULL,
    status varchar(50) NOT NULL,
    data_evento TIMESTAMP NOT NULL
);