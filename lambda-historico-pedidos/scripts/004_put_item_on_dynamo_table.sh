#!/bin/bash

TABLE_NAME=Pedidos


pedido_id=$(uuidgen)
client_id=$(uuidgen)
data_criacao=$(date -u +"%Y-%m-%dT%H:%M:%S.%6N")

echo "inserindo pedido $pedido_id..."

awslocal dynamodb put-item \
    --table-name "$TABLE_NAME" \
    --item "{
        \"pedido_id\": {\"S\": \"$pedido_id\"},
        \"client_id\": {\"S\": \"$client_id\"},
        \"valor_total\": {\"N\": \"42.99\"},
        \"status\": {\"S\": \"pendente\"},
        \"data_criacao\": {\"S\": \"$data_criacao\"}
    }"