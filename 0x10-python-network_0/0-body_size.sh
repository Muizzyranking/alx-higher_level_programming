#!/usr/bin/env bash
# script to get the size of the body of a response

curl -s "$1" | wc -c
