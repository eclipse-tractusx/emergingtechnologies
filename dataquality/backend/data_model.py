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

from dataclasses import dataclass
from copy import copy
from typing import Any

import pandas as pd
import numpy as np


@dataclass
class Metadata:
    """
    This class represents metadata for a data object.
    """
    _metadata: dict

    @property
    def metadata(self) -> dict:
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: dict):
        self._metadata = metadata

    def copy(self) -> dict:
        return self._metadata.copy()

    def __str__(self) -> str:
        return str(self.metadata)

    def __repr__(self) -> str:
        return str(self)

    def __add__(self, other: "Metadata"):
        meta = self.metadata.copy()
        meta.update(other.metadata)
        return Metadata(meta)


@dataclass
class Data:
    """
    This class represents (structured) data.
    """
    _df: pd.DataFrame
    _metadata: Metadata
    _name: str

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def df(self) -> pd.DataFrame:
        return self._df.copy()

    @property
    def metadata(self) -> dict:
        return self._metadata.copy()

    def __len__(self) -> int:
        return len(self._df)

    def __str__(self) -> str:
        str_rep = str(self._df)
        if self._metadata is not None:
            str_rep += "\n" + str(self._metadata)
        return str_rep

    def __repr__(self) -> str:
        return str(self)

    @property
    def dimension(self) -> int:
        return len(self.attributes)

    @property
    def attributes(self) -> list:
        return list(self._df.columns)

    @property
    def shape(self) -> tuple:
        return self._df.shape

    def copy(self) -> 'Data':
        return copy(self)

    def select(self, variable: str | list[str], inplace: bool = False) -> 'Data':
        """
        Selects only the columns from DataFrame with the given names and return the reduced DataFrame.

        :param variable: Name of column or list of names
        :param inplace: if inplace=True the DataFrame attribute of the current object is updated (default is False)
        :return: Data object with reduced DataFrame
        """
        if not isinstance(variable, list):
            variable = [variable]
        df_copy = self._df.copy()
        names = str.join('_', variable)
        reduced_df = df_copy[variable]
        if inplace:
            self._df = reduced_df
        return Data(reduced_df, self._metadata, self._name + f'(select {names})')

    def drop(self, variable: str | list[str], inplace: bool = False) -> 'Data':
        """
        Drop the columns from DataFrame with the given names and return the reduced DataFrame.

        :param variable: Name of column or list of names
        :param inplace: if inplace=True the DataFrame attribute of the current object is updated (default is False)
        :return: Data object with reduced DataFrame
        """
        if not isinstance(variable, list):
            variable = [variable]
        df_copy = self._df.copy()
        names = str.join('_', variable)
        reduced_df = df_copy.drop(variable, axis=1)
        if inplace:
            self._df = reduced_df
        return Data(reduced_df, self._metadata, self._name + f'(drop {names})')

    def unique_values(self, variable: str) -> np.ndarray:
        """
        Returns all existing values for the given variable.

        :param variable: Variable name
        :return: sorted existing values
        """
        return np.sort(self._df[variable].unique())

    def filter_variable_by_value(self, variable: str, value: Any, inplace: bool = False) -> 'Data':
        """
        Filter Dataframe where the given variable has one of the specified values.

        :param variable: Column name
        :param value: value or list of values to filter
        :param inplace: if inplace=True the DataFrame attribute of the current object is updated (default is False)
        :return: reduced Data object
        """
        if not isinstance(value, list):
            value = [value]
        df_copy = self._df.copy()
        reduced_df = df_copy[df_copy[variable].isin(value)]
        values_str = '[' + str.join(', ', [str(v) for v in value]) + ']'
        if inplace:
            self._df = reduced_df
        return Data(reduced_df, self._metadata, self._name + f'(Filtered {variable} = {values_str})')

    def filter_variable(self, variable: str) -> list['Data']:
        """
        Filter Dataframe by the values of the given variable. Returns one Data object per value.

        :param variable: Column name
        :return: List of Data objects, each with a single value for the given variable
        """
        df_copy = self._df.copy()
        return [Data(df_copy[df_copy[variable] == _value].drop(variable, axis=1), self._metadata,
                     self._name + f'(Filtered {variable} = {_value})') for _value in self.unique_values(variable)]

    def to_csv(self):
        """
        Convert dataframe to csv.
        :return: converted data
        """
        return self.df.to_csv(sep=';').encode('utf-8')
