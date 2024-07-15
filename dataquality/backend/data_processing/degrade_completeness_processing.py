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

import pandas as pd
from backend.data_processing.processing import Processing

import random
import numpy as np


class ProcessingDegradeCompleteness(Processing):
    """
    This class represents a processing routine that degrades the completeness of a given data set by setting a
    given fraction of cells to None.
    """
    def __init__(self, fraction: float | None = None):
        if fraction is None:
            fraction = 0.7

        parameters = dict(fraction=fraction)

        super().__init__('Degrade completeness', **parameters)

    def _process_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        _df = self._input_data.df
        _ix = [(row, col) for row in range(_df.shape[0]) for col in range(_df.shape[1])]
        for row, col in random.sample(_ix, int(round(self.parameters['fraction'] * len(_ix)))):
            _df.iat[row, col] = np.nan
        return _df
