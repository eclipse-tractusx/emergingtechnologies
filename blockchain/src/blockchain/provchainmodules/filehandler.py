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


import os
from blockchain.provchainmodules.eventmanager import EventManager
from blockchain.provchainmodules.provcollector import ProvCollector


class FileHandler:
    def __init__(self) -> None:
        self.path = os.getcwd() + '/data/files'
        self.events = EventManager()
        
    def create_txt(self, filename: str, prov_data: ProvCollector) -> None:
        filepath = f'{self.path}/{filename}.txt'
                
        with open(filepath, 'w') as file:
            file.write('')
        
        self.events.notify(prov_data)
    
    def modify_txt(self, filename: str, message: str, prov_data: ProvCollector) -> None:
        filepath = f'{self.path}/{filename}.txt'
        
        with open(filepath, 'w') as file:
            file.write(message)
            
        self.events.notify(prov_data)
    
if __name__ == '__main__':
    fh = FileHandler()
    print(fh.path)
    