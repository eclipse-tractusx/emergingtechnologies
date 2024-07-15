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
from dataclasses import dataclass
import pandas as pd
import numpy as np

from backend.data_model import Data, Metadata


@dataclass
class DataSource(ABC):
    """
    This class represents a data source f.i. a file, a database etc.
    """
    _name: str
    _parameters: dict
    _data: Data

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def data(self):
        return self._data

    @property
    def parameters(self) -> dict:
        return self._parameters

    def __init__(self, name: str, **parameters):
        self._name = name
        self._parameters = self._check_parameters(parameters)
        self._data = self._generate_data()

    @staticmethod
    def _check_parameters(parameters: dict) -> dict:
        return parameters

    def _generate_data(self) -> Data:
        return Data(self._generate_dataframe(), self._generate_meta_data(), self._generate_data_name())

    def _generate_data_name(self) -> str:
        return self.name

    def _generate_source_metadata(self) -> dict:
        return {'name': self.name, 'parameters': self.parameters}

    def _generate_meta_data(self) -> Metadata:
        return Metadata({'source': self._generate_source_metadata()})

    @abstractmethod
    def _generate_dataframe(self) -> pd.DataFrame:
        pass


class DataSourceFile(DataSource, ABC):
    def __init__(self, filename: str, file_parameters: dict,
                 name: str | None = None):
        if name is None:
            name = f'Data from file {filename}'
        super().__init__(name, **dict(filename=filename, file_parameters=file_parameters))

    @property
    def filename(self) -> str:
        return self.parameters['filename']

    @property
    def file_parameters(self) -> dict:
        return self.parameters['file_parameters']

    def _generate_dataframe(self) -> pd.DataFrame:
        return self._read_file(self.filename, self.file_parameters)

    @abstractmethod
    def _read_file(self, filename: str, file_parameters: dict) -> pd.DataFrame:
        pass


class DataSourceFileCSV(DataSourceFile):
    def _read_file(self, filename: str, file_parameters: dict) -> pd.DataFrame:
        return pd.read_csv(filename, **file_parameters)


class DataSourceNumpy(DataSource, ABC):
    def _generate_dataframe(self) -> pd.DataFrame:
        return pd.DataFrame(self._generate_numpy_array())

    @abstractmethod
    def _generate_numpy_array(self) -> np.ndarray:
        pass


class DataRandom(DataSource):
    def __init__(self, rows: int = 5, columns: int = 20, min: int = 0, max: int = 100,
                 seed=23):
        super().__init__('Random Data', **dict(rows=rows, columns=columns, min=min, max=max, seed=seed))

    def _generate_dataframe(self) -> pd.DataFrame:
        _columns = self.parameters['columns']
        _rows = self.parameters['rows']
        _min = self.parameters['min']
        _max = self.parameters['max']
        _seed = self.parameters['seed']

        np.random.seed(_seed)
        return pd.DataFrame(np.random.randint(int(_min), int(_max), size=(_rows, _columns)),
                            columns=[f'Attribute {_index}' for _index in range(_columns)])
