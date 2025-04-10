#!/bin/bash

TABLE_NAME=Pedidos

awslocal dynamodb create-table \
    --table-name "$TABLE_NAME" \
    --attribute-definitions AttributeName=pedido_id,AttributeType=S \
    --key-schema AttributeName=pedido_id,KeyType=HASH \
    --billing-mode PAY_PER_REQUEST \
    --stream-specification StreamEnabled=true,StreamViewType=NEW_AND_OLD_IMAGES