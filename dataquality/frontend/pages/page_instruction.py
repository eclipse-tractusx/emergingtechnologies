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


def page_instruction():
    """
    This page displays the demonstrator instructions.
    """

    st.title("Data Quality Service Demonstrator")

    st.subheader('Anleitung', divider='rainbow')

    _, center_col, _ = st.columns([1, 4, 2])
    with center_col:
        image_1 = Image.open('src/resources/schematics_steps_2.jpg')
        st.image(image_1, caption='Anwendungsschritte')
