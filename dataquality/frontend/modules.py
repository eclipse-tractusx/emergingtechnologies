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
from typing import Any


#
# This module provides some frontend functionality.
#


def state(key: Any | None = None):
    if key is None:
        return st.session_state
    else:
        return st.session_state[key]


def valid_state(key: Any, allow_none: bool = False) -> bool:
    if key in state():
        return state(key) is not None or allow_none
    else:
        return False


def page():
    if not valid_state('page'):
        state()['page'] = 'page_concept'

    return state('page')
