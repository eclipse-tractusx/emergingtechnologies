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

import streamlit as st
from PIL import Image
from typing import Any


def page_concept():
    """
    This page displays the demonstrator concept.
    """

    st.title("Data Quality Service Demonstrator")

    st.subheader('Konzept', divider='rainbow')

    col1, col2 = st.columns(2)
    image_1 = Image.open('src/resources/concept_1.jpg')
    image_2 = Image.open('src/resources/concept_2.jpg')
    with col1:
        st.image(image_1, caption='Anwendung als Datenqualitätsservice')
    with col2:
        st.image(image_2, caption='Anwendung als Datenraumservice')

    st.markdown('''
    * Backend: Python 
    * Frontend: Streamlit
    ''')
    st.text('')

    st.subheader('Backend', divider='rainbow')

    col1, col2 = st.columns(2)
    image_1 = Image.open('src/resources/schematics_data.jpg')
    image_2 = Image.open('src/resources/schematics_data_quality.jpg')
    with col1:
        st.image(image_1, caption='Skizze des datenseitigen Backends')
    with col2:
        st.image(image_2, caption='Skizze des datenqualitätsseitigen Backends')
