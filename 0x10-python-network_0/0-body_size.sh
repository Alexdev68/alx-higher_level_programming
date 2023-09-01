#!/bin/bash
# This script takes in a URL, sends a request to that URL, and displays the size of the body of the response
url=$1;response=$(curl -sl "$url");size=$(echo "$response" | awk '/Content-Lenght/ {print $2}');echo "$size"
