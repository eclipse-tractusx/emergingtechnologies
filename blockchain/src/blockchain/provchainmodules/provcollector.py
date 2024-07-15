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


from blockchain.utils.sha3helper import SHA3Helper


class ProvCollector:
    def __init__(self) -> None:
        self.__sender_name = None
        self.__receiver_name = None
        self.__filename = None
        self.__action = None
        
        self.prov_hash = SHA3Helper.hash256(self)
        
    def convert_to_json(self):
        return self.__dict__

    @property
    def sender_name(self):
        return self.__sender_name
    
    @sender_name.setter
    def sender_name(self, value: str):
        self.__sender_name = value
        if not isinstance(value, str):
            raise AttributeError("The sender_name has to be a string!")
    
    @property
    def receiver_name(self):
        return self.__receiver_name
    
    @receiver_name.setter
    def receiver_name(self, value: str):
        self.__receiver_name = value
        if not isinstance(value, str):
            raise AttributeError("The receiver_name has to be a string!")
    
    @property
    def filename(self):
        return self.__filename
    
    @filename.setter
    def filename(self, value: str):
        self.__filename = value
        if not isinstance(value, str):
            raise AttributeError("The filename has to be a string!")
    
    @property
    def action(self):
        return self.__action
    
    @action.setter
    def action(self, value: str):
        self.__action = value
        if not isinstance(value, str):
            raise AttributeError("The action has to be a string!")
    