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

from abc import ABC, abstractmethod
from backend.data_model import Data
from backend.report import Report


class QualityMeasures(ABC):
    """
    This abstract class represents a quality measure evaluated on data.
    """
    _name: str = ""
    _data: Data
    _report: Report
    _parameters: dict

    def __init__(self, data: Data, **parameters):
        self._data = data
        self._parameters = parameters

    @property
    def report(self) -> Report:
        return self._report

    @abstractmethod
    def measure(self, **kwargs) -> Report:
        pass

    @classmethod
    def name(cls) -> str:
        return cls._name
