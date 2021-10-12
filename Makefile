.PHONY: help check clean fetch-dependencies docker-build build-lambda-package

help:
	@python -c 'import fileinput,re; \
	ms=filter(None, (re.search("([a-zA-Z_-]+):.*?## (.*)$$",l) for l in fileinput.input())); \
	print("\n".join(sorted("\033[36m  {:25}\033[0m {}".format(*m.groups()) for m in ms)))' $(MAKEFILE_LIST)

check-versions:		## print versions of python and pip
	@python3 --version
	@pip --version

fetch-dependencies:		## install pip dependencies, download chromedriver, headless-chrome to `./bin/`
	@pip install -r requirements.txt
	@rm -rf bin/
	@mkdir -p bin/

	# ----- Get Headless-chrome ------
	curl -SL https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-29/stable-headless-chromium-amazonlinux-2017-03.zip > headless-chromium.zip
	unzip headless-chromium.zip -d bin/

	# ----- Clean -------
	@rm headless-chromium.zip
