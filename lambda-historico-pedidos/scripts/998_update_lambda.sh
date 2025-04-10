#!/bin/bash

PROJECT_NAME=lambda-historico-pedidos

awslocal lambda update-function-code \
    --function-name $PROJECT_NAME \
    --zip-file fileb://$PROJECT_NAME.zip