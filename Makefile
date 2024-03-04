.DEFAULT_TARGET := run

run: 
	python ./main.py

# setups the local dev environment with virtualenv
setup-dev:
	python -m virtualenv venv
	source venv/bin/activate
	pip install -r requirements.txt

# testing encryption
test-encrypt:
	python ./test_encrypt.py

# testing decryption
test-decrypt:
	python ./test_decrypt.py

# creates a mock os directory in os_root
create-mock:
	@for f in root home bin dev opt run var; do \
		mkdir -p os_root/$$f; \
		echo "file in os_root/$$f" > os_root/$$f/file; \
	done

# iterate the mock os directory and view the file contents
view-mock:
	@find os_root -type f -exec sh -c 'echo === {} === && cat {} && printf "\n\n"' \;
