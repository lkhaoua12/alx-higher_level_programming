#!/bin/bash
# Send the request using curl and capture the response in a variable
curl -sw '%{size_download}\n' -o /dev/null "$1"

