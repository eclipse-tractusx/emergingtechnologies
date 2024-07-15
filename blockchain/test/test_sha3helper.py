/********************************************************************************
* Copyright (c) 2024 Contributors to the Eclipse Foundation
* Copyright (c) 2024 German Aerospace Center (DLR e.V.)
*
* See the NOTICE file(s) distributed with this work for additional
* information regarding copyright ownership.
*
* This program and the accompanying materials are made available under the
* terms of the Apache License, Version 2.0 which is available at
* https://www.apache.org/licenses/LICENSE-2.0.
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
* WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
* License for the specific language governing permissions and limitations
* under the License.
*
* SPDX-License-Identifier: Apache-2.0
********************************************************************************/


from blockchain import SHA3Helper

def test_hashes_witf_same_input():
    hash_value = SHA3Helper.hash256(1)
    hash_value_2 = SHA3Helper.hash256(1)
    assert hash_value == hash_value_2

def test_hashes_with_different_input():
    hash_value = SHA3Helper.hash256(0)
    hash_value_2 = SHA3Helper.hash256(2)
    assert hash_value != hash_value_2
    