#!/bin/bash
# displays all HTTP methods that the server will accept
curl -sI "$1" | grep -i Allow | sed 's/^.*: //'
