#!/bin/bash
# show response body size
curl -s "$1" | wc -c 
