#!/bin/bash
# send the request to url passed as arg
curl -s "$1" | wc -c
