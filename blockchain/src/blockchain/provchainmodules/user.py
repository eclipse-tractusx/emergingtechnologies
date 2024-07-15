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


from blockchain.provchainmodules.filehandler import FileHandler
from blockchain.provchainmodules.provcollector import ProvCollector
from blockchain.logger.processlogger import ProcessLogger


class User:
    def __init__(self, name) -> None:
        self.name = name
        self.file_handler = FileHandler()
        self.prov_data = ProvCollector()
        self.logger = ProcessLogger("User")
        
        self.prov_data.sender_name = self.name
        
    def create_file(self, filename: str) -> None:
        self.prov_data.filename = filename
        self.prov_data.action = "File created."
        self.logger.log_info(f"User {self.name} created file {filename}.")
        self.file_handler.create_txt(filename, self.prov_data)
        
    
    def modify_file(self, filename, message):
        self.prov_data.filename = filename
        self.prov_data.action = "File modified."
        self.logger.log_info(f"User {self.name} modified file {filename} and added text {message}.")
        self.file_handler.modify_txt(filename, message, self.prov_data)
        