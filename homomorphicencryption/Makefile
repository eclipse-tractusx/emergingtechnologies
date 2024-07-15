# ********************************************************************************
# Copyright (c) 2024 Contributors to the Eclipse Foundation
# Copyright (c) 2024 German Aerospace Center (DLR e.V.)
#
# See the NOTICE file(s) distributed with this work for additional
# information regarding copyright ownership.
#
# This program and the accompanying materials are made available under the
# terms of the Apache License, Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# ********************************************************************************

SHELL = /bin/bash

PROJECT_NAME = "SecureCollaboration"
PROJECT_ROOT = .
PROJECT_ROOT_ABSOLUTE = "$(realpath ${PROJECT_ROOT})"
SOURCE_ROOT = "${PROJECT_ROOT_ABSOLUTE}/src"
PACKAGE_ROOT = "${SOURCE_ROOT}"
BUILD_ROOT = "${PROJECT_ROOT_ABSOLUTE}/build"


.PHONY: install
install: setup.py requirements.txt
	echo "[info] install"; \
	pip install -U pip; \
	pip install -e .; \

.PHONY: run
run:
	streamlit run frontend/Home.py; \

.PHONY: clean
clean:
	@echo "[info] cleaning"; \
	rm -rf ./Programs ./Player-Data; \

.PHONY: all-clean
all-clean: clean
	rm -rf ./external \

.PHONY: docker
docker: 
	docker compose up
