#!/bin/bash

# ARG 1: New Host header value
# ARG 2: Target URL
# ARG 3: Form data

curl -s \
     -X POST \
     -H "Host: $1" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "$3" \
     "$2"

