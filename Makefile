#mcandrew

PYTHON ?= python3 -W ignore

VENV_DIR := .forecast
VENV_PYTHON := $(VENV_DIR)/bin/python -W ignore

R ?= Rscript

download_data: build_env download_ili download_clinical_data download_hosp_pct_data create_iliplus

build_env:
	@echo "build forecast environment"
	@$(PYTHON) -m venv $(VENV_DIR)
	$(VENV_PYTHON) -m pip install -r requirements.txt

download_clinical_data:
	@echo "Downliading Public lab data"
	@$(R) download_lab_percentage_data.R
	@$(VENV_PYTHON) format_lab_data.py

download_ili:
	@echo "Downliading recent ili"
	@$(VENV_PYTHON) download_epidata.py

download_hosp_pct_data:
	@echo "Downloading NHSNpct hosp data"
	@$(VENV_PYTHON) download_percent_reported_hosps.py

create_iliplus:
	@echo "Create ILI+"
	@$(VENV_PYTHON) produce_ili_plus_data.py
