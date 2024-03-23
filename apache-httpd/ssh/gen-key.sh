#!/usr/bin/env bash
if [[ -z $1 ]] then
  echo "usage: ./gen-key <container-name>"
  exit 1
fi;

NAME=$1
mkdir $NAME
ssh-keygen -t rsa -q -f "./$NAME/$NAME" -N ""
