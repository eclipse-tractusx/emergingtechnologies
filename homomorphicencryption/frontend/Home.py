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

# 3rd party libraries
import streamlit as st

# add the root dir to path
import sys
sys.path.insert(0,'.')

# local imports
import components.layout


#st.set_page_config(layout="wide")
components.layout.add() # Adds logo to sidebar


#st.title("Homomorphic Encryption Demonstrator")


#file = st.file_uploader("README.md", type={"md", "txt"})
file = open('README.md','r')
st.markdown(file.read())
