#!/bin/bash -eu

while [ -n "${1+x}" ]
do
  ./upload.py "$2" "$1"
  shift 2
done