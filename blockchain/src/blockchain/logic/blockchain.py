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


import threading

from blockchain.modules.chain import Chain
from blockchain.modules.block import Block
from blockchain.utils.sha3helper import SHA3Helper


class Blockchain:
    """
    Blockchain is a class representing a blockchain structure, managing blocks, transactions,
    and ensuring that the blocks fulfill a specified difficulty requirement.

    Attributes:
        NETWORK_ID (int): An identifier for the network this blockchain belongs to.
        __chain (Chain): The underlying chain of blocks.
        __difficulty (int): The difficulty level that blocks need to fulfill.
        __block_cache (dict): A cache storing blocks with their hashes as keys.
        __transaction_cache (dict): A cache storing transactions with their IDs as keys.
    """
    NETWORK_ID = int(1)

    def __init__(self) -> None:
        self.__chain = Chain(self.NETWORK_ID)
        #self.__difficulty = int(16000)
        self.__difficulty = 57896000000000000000000000000000000000000000000000000000000000000000000
        self.__block_cache = dict()
        self.__transaction_cache = dict()
        #TODO: Check how exactly to regulate the difficulty!
        
    def __len__(self):
        return len(self.__chain.chain)
    
    def __getitem__(self, index: int):
        #TODO: Optimize to get for example JSON of the block metadata instead of an object
        block = self.__chain.chain[index]
        
        return block

    def add_block(self, block: Block):
        """
        Adds a block to the chain and updates the block and transaction caches.
        """
        self.__chain.add(block)
        self.__block_cache.update({SHA3Helper.digest_to_hex(block.get_block_hash()): block})

        for transaction in block.transactions:
            self.__transaction_cache.update({transaction[1].get_tx_id_as_string(): transaction[1]})

    def fulfills_difficulty(self, digest: bytes) -> bool:
        """
        Checks if a given digest fulfills the current difficulty requirement.
        """
        temp = int.from_bytes(digest, byteorder='big')
        #print(f"blockchain.fullfills_difficulty() Temp: {temp} Difficulty: {self.__difficulty}") # debug line
        
        return temp <= self.__difficulty

    def get_previous_hash(self) -> bytes:
        """
        Returns the hash of the last block in the chain.
        """
        return self.__chain.get_last_block().get_block_hash()
    
    def get_latest_block(self) -> Block:
        """
        Returns the latest block in the chain.
        """
        return self.__chain.get_last_block()


    @property
    def chain(self) -> Chain:
        return self.__chain
    
    @chain.setter
    def chain(self, value: Chain):
        self.__chain = value
        if value != Chain:
            raise AttributeError("The chain has to be a chain object!")
        
    @property
    def difficulty(self) -> int:
        return self.__difficulty
    
    @difficulty.setter
    def difficulty(self, value: int):
        self.__difficulty = value
        if value != int:
            raise AttributeError("The difficulty has to be an integer!")
        