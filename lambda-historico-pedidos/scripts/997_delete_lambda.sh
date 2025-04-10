#!/bin/bash

PROJECT_NAME=lambda-historico-pedidos

awslocal lambda delete-function \
    --function-name $PROJECT_NAME