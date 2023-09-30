#!/bin/bash
# curl a url and display the body size in bytes
curl -sw '%{size_download}\n' -o /dev/null "$1"
