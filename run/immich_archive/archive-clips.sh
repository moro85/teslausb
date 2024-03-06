#!/bin/bash -eu

while [ -n "${1+x}" ]
do
  ./upload.py "$2" "$1" >> /tmp/archive-error.log
  shift 2
done