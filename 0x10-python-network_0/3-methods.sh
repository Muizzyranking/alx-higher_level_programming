#!/usr/bin/bash
# displays the methods the server will accept
curl -sIL -X OPTIONS $1 | grep -i 'Allow:' 
