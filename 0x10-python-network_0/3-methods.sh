#!/bin/bash
# check allowed methods.
curl -sI  "$1" | grep -i '^Allow:' | cut -d ' ' -f 2-
