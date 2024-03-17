.PHONY: build attacker
.DEFAULT_TARGET := run

# ============= DEV SCRIPTS ===============
# setups the local dev environment with virtualenv
setup:
	python -m virtualenv venv
	source venv/bin/activate
	pip install -r requirements.txt

# runs the program locally without pyinstaller
run: 
	python ./main.py

# builds the program to a binary
build:
	echo 'building to ./dist/main'
	python -m eel main.py ui --onefile
	cp dist/main .
	rm -rf build dist main.spec

# cleans the current build
clean:
	rm -rf os_root key build dist main.spec main

# ============= ATTACKER SCRIPTS ===============
# generates the attacker's public and private key
attacker-keygen:
	cd attacker && \
	python gen-attacker-key.py

# the attacker decrypts your key with his private key and sends it back to you
attacker-decrypt:
	cd attacker && \
	python decrypt-sym-key.py

# ============= CLI MOCK OS SCRIPTS ============
# creates a mock os directory in os_root
mock-gen:
	@for f in root home bin dev opt run var; do \
		mkdir -p os_root/$$f; \
		echo "file in os_root/$$f" > os_root/$$f/file; \
	done

# iterate the mock os directory and view the file contents
mock-view:
	@find os_root -type f -exec sh -c 'echo === {} === && cat {} && printf "\n\n"' \;
