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
from io import BytesIO

import math

from backend.data_sources.data_source import DataRandom
from backend.data_processing.degrade_completeness_processing import ProcessingDegradeCompleteness
from backend.characteristics.completeness_characteristic import CompletenessCharacteristic
from backend.quality_measures.completeness_measure import (CompletenessOverall, CompletenessPerColumn,
                                                           CompletenessPerRow)

from frontend.modules import state


def page_completeness():
    """
    This page contains the demonstrator scenario for completeness evaluation.
    """
    st.title("Demonstrator Completeness")

    st.subheader('Datensatzparameter', divider='rainbow')

    st.number_input("Zeilenanzahl", min_value=1, step=1, value=100, key="datasource_num_rows")
    st.number_input("Spaltenanzahl", min_value=1, step=1, value=10, key="datasource_num_cols")
    st.text('')

    st.subheader('Modifizierungsparameter', divider='rainbow')
    st.slider("Anteil zu löschender Zellen", min_value=0., max_value=1., value=0., key="datasource_fraction")

    state()["data"] = ProcessingDegradeCompleteness(state().datasource_fraction).process(
        DataRandom(state().datasource_num_rows, state().datasource_num_cols, 0, 100).data)
    # state()["data"] = Data.get_random_data(state().datasource_num_rows, state().datasource_num_cols,
    #                                      state().datasource_fraction, state().data_name)

    # if data source exists the calculation is run
    if "data" in state():
        # first show the dataframe
        st.text('')
        st.subheader('Modifizierter Datensatz', divider='rainbow')

        # highlight the empty values in red
        def color_val(val):
            color = 'white' if not math.isnan(val) else 'red'
            return f'background-color: {color}'

        if st.toggle('Datensatz anzeigen', key='dq_completeness_show_data'):
            st.dataframe(
                state()["data"].df.style.map(color_val).format(precision=0))  # precision defines the number of digits

    if "data" in state():
        # overall completeness as pie chart
        st.text('')
        st.subheader("Report Completeness", divider='rainbow')
        # st.subheader('Overall Completeness', divider='rainbow')

        state().completeness_characteristic = CompletenessCharacteristic(state().data)
        state().completeness_results = state().completeness_characteristic.evaluate()

        state().piechart_figure = state().completeness_results.to_piechart(labels=["Leere Zellen", "Zellen mit Werten"],
                                                                           characteristic_key=CompletenessCharacteristic.
                                                                           name(),
                                                                           results_key=CompletenessOverall.name())

        # show piechart
        buf = BytesIO()
        state().piechart_figure.savefig(buf, format="png")
        _, center_col, _ = st.columns(
            [1, 6, 1])  # regularizes size, increase left and right column or reduce middle column to reduce the size
        with center_col:
            st.image(buf)

        # completeness per row and column, visualised as the original dataframe appended by a row and column
        st.subheader('Completeness pro Zeile und Spalte', divider='rainbow')

        # create and write the appended dataframe
        state().completeness_appended_df = (state().completeness_results.
                                            to_appended_data(state().data,
                                                             characteristic_key=CompletenessCharacteristic.name(),
                                                             row_key=CompletenessPerRow.name(),
                                                             column_key=CompletenessPerColumn.name(),
                                                             overall_key=CompletenessOverall.name()))
        st.dataframe(state().completeness_appended_df.df)

        # convert the dataframes for the upload
        csv_app = state().completeness_appended_df.to_csv()

        # widget to download the appended dataframe as CSV
        st.download_button(
            label="Speichere Daten als CSV",
            data=csv_app,
            file_name=f'{state().completeness_appended_df.name}.csv',
            mime='text/csv',
            key="download_df_app"
        )
    else:
        # show warning if no data source is generated or read yet
        st.warning("Please select the number of rows and columns in the sidebar and create a dataframe by pressing the "
                   "submit button before continuing.")
