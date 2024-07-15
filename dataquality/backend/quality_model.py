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

from functools import reduce
from operator import add
from typing import List, Type

from backend.characteristics.characteristic import Characteristic
from backend.data_model import Data
from backend.report import Report


class DataQualityModel:
    """
    This class defines the Data Quality Model, which consists of several quality characteristics.
    """
    _characteristics: List = [Type[Characteristic]]  # List of classes of type QualityMeasures
    _name: str = ""   # Name of the quality model used in the report
    _data: Data  # data that is analyzed
    _report: Report  # Report object of the results

    def __init__(self, data: Data):
        self._data = data

    def evaluate(self, args) -> Report:
        """
        Evaluates the model by evaluating all the characteristics for the given data and returns the results as
        a report.

        :param args: List of lists containing dictionary's, one list for each characteristic, they contain the arguments
         for the measurement
        :return: Report object with the results
        """
        results_report = reduce(add, [reduce(add, [self._characteristics[i](self._data).evaluate(**charargs[i])
                                      for i in range(len(charargs))]) for charargs in args])
        self._report = Report({self._name: results_report.results})
        return self.report

    @property
    def report(self):
        return self._report

    @classmethod
    def name(cls):
        return cls._name

    @classmethod
    def characteristics(cls):
        """
        Returns the quality measures used in the model.

        :return: List of quality measures
        """
        return cls._characteristics
