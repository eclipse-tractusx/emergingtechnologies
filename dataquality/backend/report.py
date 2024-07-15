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

import numbers
from typing import List

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from backend.data_model import Data


class Report:
    """
    The report class wraps the results of routines in a dictionary and offers methods to use and process the results.
    Its structure is hierarchical, the value for a quality model is again a dictionary. The keys describe the different
    characteristics and the value the measurements for them.
    """
    _results: dict

    def __init__(self, results: dict):
        self._results = results

    def __add__(self, other: "Report"):
        """
        Adding two reports merges the dictionary's to one
        :param other: second dictionary
        :return: new Report object containing the merged results
        """
        merged_results = {**self._results, **other.results}
        return Report(merged_results)

    @property
    def results(self) -> dict:
        """
        Property that returns the results
        :return: dictionary containing results
        """
        return self._results

    @property
    def name(self) -> str:
        """
        Property that returns the name
        :return: string containing name
        """
        return self._results['name']

    @property
    def name_readable(self) -> str:
        """
        Property that returns the user readable name
        :return: string containing user readable name
        """
        return self._results['name_readable']

    @property
    def type(self) -> str:
        """
        Property that returns the report type
        :return: string containing report type
        """
        return self._results['type']

    def sub_report(self, attribute: str) -> 'Report':
        """
        Return a sub-report.
        :return: Report containing sub-report results
        """
        if attribute in self._results.keys():
            if isinstance(self._results[attribute], dict):
                _result = Report(self._results[attribute])
                return Report(self._results[attribute])
            else:
                return Report({})
        else:
            return Report({})

    def to_print(self) -> str:
        """This function converts the dictionary to a string that can be printed to show the results."""
        return_str = ""
        num_tabs = 0
        for key, value in self._results.items():
            # quality model, characteristic or result
            if type(value) == dict:
                # characteristic or result
                return_str += str(key) + ":\n"
                num_tabs += 1
                for l1key, l1value in value.items():
                    if type(l1value) == dict:
                        # result
                        return_str += "".join(["\t"] * num_tabs) + str(l1key) + ":\n"
                        num_tabs += 1
                        for l2key, l2value in l1value.items():
                            return_str += "".join(["\t"] * num_tabs) + str(l2key) + ": " + str(l2value) + "\n"
                        num_tabs -= 1
                    else:
                        return_str += "".join(["\t"] * num_tabs) + str(l1key) + ": " + str(l1value) + "\n"
                num_tabs -= 1
            else:
                return_str += "".join(["\t"] * num_tabs) + str(key) + ": " + str(value) + "\n"
        return return_str

    def to_table(self, parameter) -> pd.DataFrame:
        pass

    def to_piechart(self, labels=List[str], quality_model_key: str | None = None, characteristic_key: str | None = None,
                    results_key: str | None = None, autopct='%1.1f%%') -> plt.figure:
        """
        This function converts results in the dictionary to a pie chart.

        :param labels: Labels for the fractions in the pie chart
        :param quality_model_key: Name of the quality model as string or None, used to address the characteristics
        :param characteristic_key: Name of the characteristic model as string or None, used to address the results
        :param results_key: Name of the result
        :param autopct: attribute of the pie chart function that defines the format of the labels, default is 1.1f
        :return: matplotlib.pyplot.figure object that shows the pie chart
        """
        if quality_model_key is not None:
            results = self.results[quality_model_key]
            if characteristic_key is not None:
                results = results[characteristic_key]
                results = results[results_key]
        elif characteristic_key is not None:
            results = self.results[characteristic_key]
            results = results[results_key]
        else:
            results = self.results[results_key]

        if not isinstance(results, List) and not isinstance(results, numbers.Number):
            raise AttributeError("To create a piechart the results must be either a list of values or one single "
                                 "value.")

        if isinstance(results, numbers.Number):
            results = [1. - results, results]

        fig, ax = plt.subplots()
        ax.pie(results, labels=labels, autopct=autopct)
        return fig

    def to_appended_data(self, data: Data, quality_model_key: str | None = None, characteristic_key: str | None = None,
                         row_key: str | None = None, column_key: str | None = None,
                         overall_key: str | None = None) -> Data:
        """
        Create new data object appended by results that either contain the row results or column results or both
        in combination with the overall measure.

        :param data: Data object that gets appended
        :param quality_model_key: Name of the routine if the report is the report of a routine, otherwise None
        :param characteristic_key: Name of the characteristic if the report is the report of a characteristic,
        otherwise None
        :param row_key: Name of the measure that contains the results per row or None
        :param column_key: Name of the measure that contains the results per column or None
        :param overall_key: Name of the measure that contains the results over the whole dataframe
        :return: Data object
        """

        # first extract the necessary dictionary to get access to the results
        if quality_model_key is not None:
            results = self.results[quality_model_key]
            if characteristic_key is not None:
                results = results[characteristic_key]
        elif characteristic_key is not None:
            results = self.results[characteristic_key]
        else:
            results = self.results

        # create a copy of the input
        appended_df = data.df.copy()

        # add both row and column
        if column_key is not None and row_key is not None:
            result_pc = results[column_key]
            result_pr = results[row_key]
            result_overall = results[overall_key]
            results_pc_temp = np.append(result_pc, result_overall)
            appended_df.loc[:, row_key] = pd.Series(result_pr)
            appended_df = pd.concat([appended_df, pd.DataFrame([results_pc_temp], index=[column_key],
                                                               columns=appended_df.columns)], axis=0)
        # add only columns results as new row
        elif column_key is not None:
            result_pc = results[column_key]
            appended_df = pd.concat([appended_df, pd.DataFrame([result_pc], index=[column_key],
                                                               columns=appended_df.columns)], axis=0)
        # add only rows results as new column
        elif row_key is not None:
            result_pr = results[row_key]
            appended_df.loc[:, row_key] = pd.Series(result_pr)

        return Data(appended_df, data.metadata, data.name + "_" + characteristic_key)
