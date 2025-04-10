#!/bin/bash

TABLE_NAME=Pedidos

awslocal dynamodb scan \
    --table-name "$TABLE_NAME"