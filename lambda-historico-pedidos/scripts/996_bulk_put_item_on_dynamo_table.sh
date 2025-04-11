#!/bin/bash

seq 1 500 | xargs -n1 -P10 bash ./scripts/004_put_item_on_dynamo_table.sh