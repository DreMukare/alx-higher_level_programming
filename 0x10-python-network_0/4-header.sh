#!/bin/bash
# displays body of response to GET request
curl -sL "$1" -X GET -H "X-HolbertonSchool-User-Id: 98"
