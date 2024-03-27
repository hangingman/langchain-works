SHELL=/usr/bin/env bash

.PHONY: install
install:
	pip install pip-tools
	pip-sync requirements.txt
	pip install .

.PHONY: install-dev
install-dev:
	pip install pip-tools
	pip-sync requirements.txt requirements-dev.txt
	pip install -e .

.PHONY: pin
pin:
	pip install pip-tools
	pip-compile requirements.in -o requirements.txt
	pip-compile requirements-dev.in -o requirements-dev.txt

# black との兼ね合いで E501 が disable されるが、black だけだと lint ができなくて不便なので enable しておく
.PHONY: pysen-configure
pysen-configure:
	pysen generate .
	sed -i setup.cfg -e 's/ignore = E203,E231,E501,W503/ignore = E203,E231,W503/g'

# pysen run lint がうまく階層を掘ってくれないので、それぞれ個別に実行
.PHONY: lint
lint:
	black --config pyproject.toml --diff --check tests/ mini_qa/
	flake8 --config setup.cfg tests/ mini_qa/
	isort --settings-path pyproject.toml --diff --check-only tests/ mini_qa/
	mypy --show-absolute-path --pretty --config-file setup.cfg tests/ mini_qa/

# pysen run format がうまく階層を掘ってくれないので、それぞれ個別に実行
.PHONY: format
format:
	black --config pyproject.toml tests/ mini_qa/
	isort --settings-path pyproject.toml tests/ mini_qa/

.PHONY: test
test:
	pytest tests/
