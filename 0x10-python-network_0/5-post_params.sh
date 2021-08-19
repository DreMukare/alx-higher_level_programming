#!/bin/bash
# sends a POST request and displays body of response
curl -s -X POST -d "email=hr@holbertonschool.com&subject=I will always be there for PLD" "$1"
