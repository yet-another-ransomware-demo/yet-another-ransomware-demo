.PHONY: build attacker
.DEFAULT_TARGET := run

# ============= DEV SCRIPTS ===============
# runs the program locally without pyinstaller
run: 
	python ./main.py

# builds the program to a binary
build:
	echo 'building to ./dist/main'
	pyinstaller -n 'ransomware' --onefile main.py

# cleans the current build
clean:
	rm -rf os_root key build dist ransomware.spec ransomware

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
