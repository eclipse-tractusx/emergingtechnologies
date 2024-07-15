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


from typing import List
from copy import deepcopy

from blockchain.modules.block import Block
from blockchain.modules.genesisblock import GenesisBlock


class Chain:
    """
    The chain object collects the blocks.
    
    Attributes:
            __chain (List[Block]): The list of blocks in the chain, initialized with the genesis block.
            __network_id (int): The identifier for the network.
    """
    def __init__(self, network_id: int) -> None:
        self.__chain: List[Block] = [GenesisBlock()]
        #self.__chain = list()
        self.__network_id = network_id

    def add(self, block: Block) -> None:
        """
        Add a block to the chain.
        """
        self.__chain.append(block)
    
    def get_block(self, index: int) -> Block:
        """
        Get block of the chain by index.
        """
        return self.__chain[index]

    def get_last_block(self) -> Block:
        """
        Get the last block of the chain.
        """        
        return self.__chain[-1]

    def get_size(self) -> int:
        """
        Get the number of blocks that are on the chain.
        """
        return len(self.__chain)

    @property
    def network_id(self):
        return self.__network_id

    @network_id.setter
    def network_id(self, value: int):
        self.__network_id = value
        if value != int:
            raise AttributeError("The network id has to be an integer!")
    
    @property
    def chain(self) -> List[Block]:
        return deepcopy(self.__chain)


    @chain.setter
    def chain(self, value: list):
        self.__chain = value
        if value != list:
            raise AttributeError("The chain has to be a list!")


    #! @override is missing -> see Java class
    