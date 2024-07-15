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

from frontend.pages.page_completeness import page_completeness
from frontend.pages.page_concept import page_concept
from frontend.pages.page_instruction import page_instruction
from frontend.modules import state, page

#
# Main dashboard. Calls the different pages of the demonstrator.
#


def scenario_completeness():
    state()['page'] = 'page_completeness'


def information_concept():
    state()['page'] = 'page_concept'


def information_instruction():
    state()['page'] = 'page_instruction'


def main():
    # create session state
    st.set_page_config(page_title='Demonstrator Data Quality')

    with st.sidebar:
        st.subheader('Szenarios', divider='rainbow')
        st.button('Completeness', use_container_width=True, key='1', on_click=scenario_completeness,
                  help='Szenario zum Vorstellen der Datenqualitätscharakteristik \"Completeness\"')
        st.button('Syntactic Accuracy', use_container_width=True, key='2', disabled=True)
        st.button('Currentness', use_container_width=True, key='3', disabled=True)

        st.subheader('Informationen', divider='rainbow')
        st.button('Konzept', use_container_width=True, key='k', on_click=information_concept)
        st.button('Anleitung', use_container_width=True, key='a', on_click=information_instruction)

        st.subheader('', divider='rainbow')
        st.markdown('''<span style="font-size:10pt;">&copy; DLR 2024<br>
        <a href="https://www.dlr.de/de/ki" target=”_blank”>Institut für KI-Sicherheit</a><br>
        <a href="https://www.dlr.de/de/ki/ueber-uns/abteilungen/sicherheitskritische-dateninfrastrukturen"
         target=”_blank”>Sicherheitskritische Dateninfrastrukturen</a>
        </span>
        ''', unsafe_allow_html=True)

    if page() == 'page_completeness':
        page_completeness()
    elif page() == 'page_concept':
        page_concept()
    elif page() == 'page_instruction':
        page_instruction()
