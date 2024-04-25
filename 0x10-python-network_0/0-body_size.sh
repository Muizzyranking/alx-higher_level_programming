#!/usr/bin/env bash
# script to get the size of the body of a response

URL="$1"

curl -s $URL | wc -c
