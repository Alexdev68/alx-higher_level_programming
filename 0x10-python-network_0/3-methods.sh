#!/bin/bash
# This is a script that takes in a URL and displays all HTTP methods the server will accept.
curl -sI OPTIONS "$1" | awk -F ': ' '/^Allow:/ {print $2}'
