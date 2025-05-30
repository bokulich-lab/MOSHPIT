.PHONY: all lint test install dev clean distclean

PYTHON ?= python
PREFIX ?= $(CONDA_PREFIX)

all: ;

lint:
	q2lint
	flake8

test: all
	pytest

install: all
	$(PYTHON) -m pip install -v . && \
	mkdir -p $(PREFIX)/etc/conda/activate.d && \
	cp hooks/50_activate_mosh_tab_completion.sh $(PREFIX)/etc/conda/activate.d/

dev: all
	pip install -e . && \
	mkdir -p $(PREFIX)/etc/conda/activate.d && \
	cp hooks/50_activate_mosh_tab_completion.sh $(PREFIX)/etc/conda/activate.d/

clean: distclean

distclean: ;
