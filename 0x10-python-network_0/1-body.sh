#!/bin/bash
# takes URL as arg, sends GET request to URL, displays size of body of response
curl -sL "$1"
