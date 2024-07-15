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

from operator import add
from functools import reduce
from typing import List, Type

from backend.quality_measures.quality_measures import QualityMeasures
from backend.report import Report
from backend.data_model import Data


class Characteristic:
    """
    This class represents a quality characteristic that is determined by one or more quality measures.
    """
    _measures: List = [Type[QualityMeasures]]  # List of classes of type QualityMeasures
    _name: str = ""  # Name of the characteristic used for the report
    _data: Data  # data that is analyzed
    _report: Report  # Report object of the results

    def __init__(self, data: Data):
        self._data = data

    def evaluate(self, args: List | None = None) -> Report:
        """
        Evaluates the characteristic by measuring all the quality measures for the given data and returns the results as
        a report.

        :param args: List of dictionary's, one for each quality measure, they contain the arguments for the measurement,
        if args=None, the default parameters for all measures are used
        :return: Report object with the results
        """
        if args is None:
            args = [dict() for i in range(len(self._measures))]
        results_report = reduce(add, [self._measures[i](self._data).measure(**args[i])
                                      for i in range(len(self._measures))])
        self._report = Report({self._name: results_report.results})
        return self.report

    @property
    def report(self) -> Report:
        return self._report

    @classmethod
    def name(cls) -> str:
        return cls._name

    @classmethod
    def measures(cls) -> List[Type[QualityMeasures]]:
        return cls._measures
