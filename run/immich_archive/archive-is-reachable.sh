#!/bin/bash -eu

curl -L 'https://"$1"/api/server-info/ping' \
-H 'Accept: application/json'