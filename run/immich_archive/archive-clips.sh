#!/bin/bash -eu

while [ -n "${1+x}" ]
do
  echo "$2" "$1" >> "$LOG_FILE"
  /root/bin/upload.py "$2" "$1" >> "$LOG_FILE" 2>&1
  shift 2
done