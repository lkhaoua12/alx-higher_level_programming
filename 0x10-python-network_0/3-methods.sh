#!/bin/bash
# check allowed methods.
curl -sI  "$1" | sed -n '/Allow: /s/Allow: //p'
