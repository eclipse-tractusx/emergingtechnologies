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

from backend.quality_measures.quality_measures import QualityMeasures
from backend.report import Report


class CompletenessPerRow(QualityMeasures):
    """
    This class represents a quality measure that evaluates the completeness per row.
    """
    _name: str = "Completeness per row"

    def measure(self, variable: str | list[str] | None = None) -> Report:
        """
        Calculates completeness per row.

        :param variable: variable name or list of variable names, default is none, so it's calculated for all variables
        :return: Report object containing the result
        """
        # no variable defined
        if variable is None:
            compl = [1. - row.isna().sum() / len(self._data.df.columns) for i, row in self._data.df.iterrows()]
        else:
            if not isinstance(variable, list):
                variable = list[variable]
            compl = [1. - row.isna().sum() / len(self._data.df.columns) for i, row in self._data.df.iloc[variable]]
        self._report = Report({self._name: compl})
        return self.report


class CompletenessPerColumn(QualityMeasures):
    """
    This class represents a quality measure that evaluates the completeness per column.
    """
    _name: str = "Completeness per column"

    def measure(self, variable: str | list[str] | None = None) -> Report:
        """
        Calculates completeness per column.

        :param variable: variable name or list of variable names, default is none, so it's calculated for all variables
        :return: Report object containing the result
        """
        # no variable defined
        if variable is None:
            compl = [1. - self._data.df[var].isnull().sum() / len(self._data.df[var])
                     for var in self._data.df.columns]

        self._report = Report({self._name: compl})
        return self.report


class CompletenessOverall(QualityMeasures):
    """
    This class represents a quality measure that evaluates the total completeness.
    """
    _name: str = "Completeness overall"

    def measure(self, variable: str | list[str] | None = None) -> Report:
        """
        Calculates completeness overall.

        :param variable: variable name or list of variable names, default is none, so it's calculated for all variables
        :return: Report object containing the result
        """
        df_nan_count = self._data.df.isna().sum().sum()
        compl = 1. - df_nan_count / self._data.df.size
        self._report = Report({self._name: compl})
        return self.report
