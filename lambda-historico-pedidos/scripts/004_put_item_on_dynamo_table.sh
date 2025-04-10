#!/bin/bash

TABLE_NAME=Pedidos

awslocal dynamodb put-item \
    --table-name "$TABLE_NAME" \
    --item '{
        "pedido_id": {
            "S": "12411014531-1432-411-919a-2795735141"
        },
        "client_id": {
            "S": "60406360-13dc-4dee-9e8d-fc2205960c42"
        },
        "valor_total": {
            "N": "42.99"
        },
        "status": {
            "S": "pendente"
        },
        "data_criacao": {
            "S": "1744246138"
        }
    }'