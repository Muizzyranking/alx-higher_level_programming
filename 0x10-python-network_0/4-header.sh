#!/bin/bash
# takes a url, send a GET request to the URL, and displays the body of the response
curl -sH "X-School-User-Id: 98" "$1"
