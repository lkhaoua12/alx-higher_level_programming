#!/bin/bash
# Send the request using curl and capture the response in a variable
response=$(curl -sI "$1")
# Extract the content length from the response headers
content_length=$(echo "$response" | grep -i 'Content-Length' | awk '{print $2}' | tr -d '\r\n')
echo "$content_length"
