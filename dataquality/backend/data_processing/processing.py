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

from abc import abstractmethod, ABC
from dataclasses import dataclass
import pandas as pd

from backend.data_model import Data, Metadata


@dataclass
class Processing(ABC):
    """
    This class represents a processing routine on a Data object, generating another Data object.
    Any processing algorithm can be encapsulated.
    """
    _name: str
    _parameters: dict

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def parameters(self) -> dict:
        return self._parameters

    @property
    def input_data(self) -> Data | None:
        return self._input_data

    def data(self) -> Data | None:
        return self._output_data

    def __init__(self, name: str, **parameters):
        self._name = name
        self._parameters = parameters
        self._input_data = None
        self._output_data = None

    def _process_data(self) -> Data:
        return Data(self._process_dataframe(self._input_data.df), self._process_metadata(self._input_data.metadata),
                    self._process_name(self._input_data.name))

    @staticmethod
    def _process_metadata(metadata: Metadata) -> Metadata:
        return metadata

    @staticmethod
    def _process_name(name: str) -> str:
        return name

    @abstractmethod
    def _process_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        pass

    def process(self, data: Data) -> Data:
        self._input_data = data
        self._output_data = self._process_data()
        return self._output_data
