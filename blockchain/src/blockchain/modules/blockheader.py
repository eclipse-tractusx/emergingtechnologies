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

class BlockHeader:
    """
    The Block Header is the most importent part of every block. It contains the
    metadata information about the block, like version of the blokchain or the 
    nonce for the cryptographic puzzle. It is also used to calculate the block_id.
    
    Attributes:
            timestamp (int): Timestamp of the block when created.
            previous_hash (bytes): Hash of the previous block.
            transaction_list_hash (bytes): Hash of the hole transaction list. Merkle root.
    """
    def __init__(self, timestamp: int, previous_hash: bytes, transaction_list_hash: bytes) -> None:
        self.__version = 1
        self.__timestamp = timestamp
        self.__previous_hash = previous_hash
        self.__transaction_list_hash = transaction_list_hash
        self.__nonce = 1

    def increment_nonce(self) -> None:
        """
        Increment root to find fitting nonce for crypto puzzle.
        """
        if self.__nonce >= (2 ** 31) - 1:       # calculates the "maximum" value of an integer 
            raise ArithmeticError("nonce too high")

        self.__nonce += 1

    def as_hash(self) -> bytes:
        """
        Get hash of the blockheader instance.
        """
        return SHA3Helper.hash256(self)
    
    def to_json(self) -> dict:
        return dict(version = self.__version,
                    timestamp = self.__timestamp,
                    previous_hash = self.__previous_hash,
                    #transaction_list_hash = self.__transaction_list_hash.decode(), #! Some bug is here. Says hash hasn't the 'utf-8' format! 
                    nonce = self.__nonce
                    )

    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, value: int):
        self.__version = value
        if value != int:
            raise AttributeError("The version number has to be an integer!")

    @property
    def timestamp(self):
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, value: int):
        self.__timestamp = value
        if value != int:
            raise AttributeError("The timestamp has to be an integer!")

    @property
    def previous_hash(self):
        return self.__previous_hash

    @previous_hash.setter
    def previous_hash(self, value: bytes):
        self.__previous_hash = value
        if value != bytes:
            raise AttributeError("The Previous Hash has to be in bytes!")

    @property
    def transaction_list_hash(self):
        return self.__transaction_list_hash

    @transaction_list_hash.setter
    def transaction_list_hash(self, value: bytes):
        self.__transaction_list_hash = value
        if value != bytes:
            raise AttributeError("The transaction list hash has to be in bytes!")

    @property
    def nonce(self):
        return self.__nonce

    @nonce.setter
    def nonce(self, value: int):
        self.__nonce = value
        if value != int:
            raise AttributeError("The nonce has to be an integer!")
