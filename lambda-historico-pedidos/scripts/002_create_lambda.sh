#!/bin/bash

PROJECT_NAME=lambda-historico-pedidos

awslocal lambda create-function \
    --function-name $PROJECT_NAME \
    --runtime python3.12 \
    --zip-file fileb://$PROJECT_NAME.zip \
    --handler src.interfaces.aws.lambda_handler.lambda_handler \
    --role arn:aws:iam::000000000000:role/lambda-role \
    --environment Variables="{PYTHONPATH=/var/task/src,DATABASE_URL=postgresql://postgres:mypassword@postgres:5432/postgres}"