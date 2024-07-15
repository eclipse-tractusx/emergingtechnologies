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


from time import time

from blockchain.modules.blockheader import BlockHeader
from blockchain.modules.transaction import Transaction
from blockchain.utils.sha3helper import SHA3Helper


class Block:
    """
    A block is a main part of the chain. It has two important components, the block header
    and the list of transactions. Each block contains his own block header with some
    information about the block. 
    
    Attributes:
            transactions (list): List of transactions in the block.
            previous_hash (bytes): Hash of the previous block.
    """
    def __init__(self, transactions: list, previous_hash: bytes) -> None:
        # self.__block_size = None #! See how to solve this in Python
        self.__transactions = transactions
        self.__transaction_count = 0
        self.__block_header = BlockHeader(int(time()*1000), previous_hash, self.transaction_hash()) 
    
    def transaction_hash(self) -> bytes:
        """
        Build the merkle root out of all transactions in the list.
        """
        transactions_in_bytes = bytearray()

        for transaction in self.__transactions:
            transactions_in_bytes.extend(transaction[1].tx_id)  # 'transaction' are tuple because of priorityQueue
            
        return SHA3Helper.hash256(transactions_in_bytes)
    
    def add_transaction(self, transaction: Transaction) -> None:
        """
        Add transaction to the transaction list.
        """
        self.__transactions.append(transaction)
        self.__transaction_count += 1
        self.__block_header.transaction_list_hash.replace(self.__block_header.transaction_list_hash, self.transaction_hash()) #! Look if this is right transaction_list_hash datatype bytes()
        print("Transaction list hash", self.__block_header.transaction_list_hash)
        #self.block_size = 128 #! How to do this in python?

    def to_json(self) -> dict:
        return dict(transactions = self.__transactions,
                    transaction_counts = self.__transaction_count,
                    block_header = self.__block_header
                    )

    def get_block_hash(self) -> bytes:
        return self.__block_header.as_hash()
    
    def increment_nonce(self) -> None:
        self.__block_header.increment_nonce()

    @property
    def transactions(self) -> list:
        return self.__transactions
    
    @transactions.setter
    def transactions(self, value: list):
        self.__transactions = value
        if value != list:
            raise AttributeError("The transactions have to be in a list!")

    @property
    def transaction_count(self) -> int:
        return self.__transaction_count
    
    @transaction_count.setter
    def transaction_count(self, value: int):
        self.__transaction_count = value
        if value != int:
            raise AttributeError("The transaction count has to be an integer!")

    @property
    def block_header(self) -> BlockHeader:
        return self.__block_header
    
    @block_header.setter
    def block_header(self, value: BlockHeader):
        self.__block_header = value
        if value != BlockHeader:
            raise AttributeError("The block_header has to be a block_header object!")
