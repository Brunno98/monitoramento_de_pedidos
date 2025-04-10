#!/bin/bash

awslocal lambda invoke \
    --function-name customer-suspension-consumer \
    output.txt