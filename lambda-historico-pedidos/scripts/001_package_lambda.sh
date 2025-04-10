#!/bin/bash

PROJECT_NAME=lambda-historico-pedidos

mkdir package

pip install --target ./package -r requirements.txt

cd package
zip -r ../$PROJECT_NAME.zip .

cd ..
zip -r $PROJECT_NAME.zip src/*