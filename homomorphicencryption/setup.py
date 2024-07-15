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


from setuptools import setup
import os

# read version file
# exec(open("src/version.py").read())
__version__ = "0.0.1.dev0"


def readme():
    with open("README.md", "r") as f:
        return f.read()


extras_require = {
    "dev": [
        # linting and static type-checking
        "autopep8~=2.0.2",
        "coverage~=7.2.7",
        "flake8~=6.0.0",
        "mypy~=1.3.0",
        # documentation
#        "pdoc3~=0.10.0",  # cspell:ignore pdoc
        # others
        "pre-commit~=3.3.2",
        "tox~=4.5.1",  # used to generate license info via `make licenses`
    ],
}

setup(
    name="DLR Streamlit Demo Template",
    version=__version__,  # type: ignore  # noqa: F821
    description="DLR Streamlit Demo Template",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="[[Your GITLab Repo Link Here]]",
    packages=["src"],
    package_dir={
        "src": "src"
    },
    python_requires=">=3.10",
    install_requires=[
        "scikit-learn",
        "streamlit",
        "psutil",
        "streamlit-elements",
        "streamlit-folium",
        "streamlit-extras",
        "streamlit-agraph",
        "toml",
        "streamlit-image-coordinates",
        "streamlit-javascript",
        "st-pages",
        "vpython"
    ],
    extras_require=extras_require,
    classifiers=[
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering",
    ],
)
