#!/bin/bash

TABLE_NAME=Pedidos
FUNCTION_NAME=lambda-historico-pedidos

LATEST_STREAM_ARN=$(awslocal dynamodb describe-table --table-name "$TABLE_NAME" \
    | grep '"LatestStreamArn"' \
    | cut -d '"' -f4 \
)


awslocal lambda create-event-source-mapping \
    --function-name "$FUNCTION_NAME" \
    --event-source "$LATEST_STREAM_ARN"  \
    --batch-size 1 \
    --starting-position TRIM_HORIZON