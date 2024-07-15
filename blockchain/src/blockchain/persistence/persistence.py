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
import codecs
import json

from blockchain.modules.block import Block
from blockchain.modules.chain import Chain
from blockchain.utils.sha3helper import SHA3Helper
from blockchain.utils.complexencoder import ComplexEncoder

class Persistence:
    def __init__(self) -> None:
        self.__encoding = "utf-8"
        self.__path = os.getcwd() + "/chains"

        self.file = self.create_file()

    def create_file(self) -> None:
        if not os.path.exists(self.__path):
            os.mkdir(self.__path)

    def write_chain(self, chain: Chain):
        network_id = chain.network_id
        if self.does_chain_not_exist(network_id):
            self.creat_chain(network_id)

        for block in chain.chain:
            block_id = str(SHA3Helper.digest_to_hex(block.block_header.as_hash())) #! original code has a getHash method but why?
            
            if self.file_does_not_exist(network_id, block_id):
                self.write_block(block, network_id, block_id)

    def does_chain_not_exist(self, network_id: int) -> bool:
        chain_path = self.get_path_to_chain(network_id)
        return not os.path.exists(chain_path)
    
    def creat_chain(self, network_id: int) -> None:
        directory_path = self.get_path_to_chain(network_id)

        try:
            os.mkdir(directory_path)
            print("Building chain succeeded.")
        except IOError as e:
            print("Error building chain:")
            print(e)

    def file_does_not_exist(self, network_id: int, id: str) -> bool:
        block_path = self.get_path_to_block(network_id, id)
        return not os.path.exists(block_path)

    def write_block(self, block: Block, network_id: int, block_id: str) -> None:
        file_path = self.get_path_to_block(network_id, block_id)
        json_format = json.dumps(block.to_json(), cls=ComplexEncoder, indent=4) #* indent can be removed
        print(json_format) #* println for demonstration of json

        try:
            with open(file_path, 'w', encoding=self.__encoding) as file:
                json.dump(json_format, file)
        except IOError as e:
            print("Error writting block:")
            print(e)

    def read_chain(self, network_id) -> Chain:
        chain = Chain(network_id)

        if self.does_chain_exist(network_id):
            chain_path = self.get_path_to_chain(network_id)
            files = os.listdir(chain_path)

            for file in files:
                block = self.read_block(os.path.join(chain_path, file))
                chain.add(block)

        return chain

    def does_chain_exist(self, network_id: int) -> bool:
        chain_path = self.get_path_to_chain(network_id)
        return os.path.exists(chain_path)

    def read_block(self, file) -> Block:
        with open(file, 'r', encoding=self.__encoding) as file:
            block_data = json.load(file)
            block = Block(block_data.transactions) #TODO: Look how to deserialize objects!

        return block

    def get_path_to_chain(self, network_id: int) -> str:
        return os.path.join(self.path, str(network_id))

    def get_path_to_block(self, network_id: int, block_id: str) -> str:
        fileName = block_id + '.json'
        return os.path.join(self.path, str(network_id), fileName)
    
    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, value: str):
        self.__path = value
        if value != str:
            raise AttributeError("The path has to be a string!")
