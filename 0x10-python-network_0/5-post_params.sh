#!/bin/bash
# sends a POST request and displays body of response
curl -sL "$1" -X POST -d "email=hr@holbertonschool.com&subject=I will always be there for PLD"
