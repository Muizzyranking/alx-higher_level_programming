#!/bin/bash
# takes URL as arg, sends GET request to URL, displays size of body of response
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
