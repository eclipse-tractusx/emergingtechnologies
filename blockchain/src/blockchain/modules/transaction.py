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

class Transaction:
    """
    A transaction object takes all information about the transaction. The transaction
    information that are also the arguments get serilized to hash them.
    
    Args:
    sender  : Add hash of the sender.
    reciever: Add hash of the receiver.
    amount  : Amount of value of transaction.
    nonce   : __description__
    transaction_fee_base_price: Fee base price for the transaction
    transaction_fee_limit: Fee limit for the transaction.
    """  
    def __init__(self, sender: bytes, receiver: bytes, amount: float, nonce: int, 
    transaction_fee_base_price: float, transaction_fee_limit: float, prov_hash) -> None:
        self.__sender = sender
        self.__receiver = receiver
        self.__amount = amount
        self.__nonce = nonce
        self.__transaction_fee_base_price = transaction_fee_base_price
        self.__transaction_fee_limit = transaction_fee_limit
        self.prov_hash = prov_hash #* new attribute for ProvChain demo

        self.__block_id = 0
        
        self.__tx_id = SHA3Helper.hash256(self)
        #TODO: Add attribute for data example to transfer with transaction
    
    def get_tx_id_as_string(self) -> str:
        """
        Convert tx_id from hash to string.
        """
        return SHA3Helper.hash256_as_hex(self)
    
    def to_json(self) -> dict:
        """
        Put transaction attributes sender, receiver, amount, nonce,
        transaction_fee_base_price and transaction_fee_limit in a 
        dictonary to make them JSON compatible.
        """
        return dict(sender = self.__sender,
                    receiver = self.__receiver,
                    amount = self.__amount,
                    nonce=self.__nonce,
                    transaction_fee_base_price = self.__transaction_fee_base_price,
                    transaction_fee_limit = self.__transaction_fee_limit
                    )

    # take out attributes from serialization
    def __getstate__(self):
        state = self.__dict__.copy()
        if '__block_id' in state:   
            del state['__block_id'] #* exclude 'block_id' from serialization
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.__block_id = 0  #* set 'block_id' to default value

    
    def __getstate__(self):
        state = self.__dict__.copy()
        if '__tx_id' in state:
            del state['__tx_id'] 
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.__tx_id = SHA3Helper.hash256(self) 
    

    @property
    def sender(self):
        return self.__sender

    @sender.setter
    def sender(self, value: bytes):
        self.__sender = value
        if value != bytes:
            raise AttributeError("The sender has to be in byte format!")

    @property
    def receiver(self):
        return self.__receiver

    @receiver.setter
    def receiver(self, value: bytes):
        self.__receiver = value
        if value != bytes:
            raise AttributeError("The receiver has to be in byte format!")

    @property
    def receiver(self):
        return self.__receiver

    @receiver.setter
    def receiver(self, value: bytes):
        self.__receiver = value
        if value != bytes:
            raise AttributeError("The receiver has to be in byte format!")

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value: float):
        self.__amount = value
        if value != float:
            raise AttributeError("The amount has to be a float value!")

    @property
    def nonce(self):
        return self.__nonce

    @nonce.setter
    def nonce(self, value: int):
        self.__nonce = value
        if value != int:
            raise AttributeError("The nonce has to be a int value!")

    @property
    def transaction_fee_base_price(self):
        return self.__transaction_fee_base_price

    @transaction_fee_base_price.setter
    def transaction_fee_base_price(self, value: float):
        self.__transaction_fee_base_price = value
        if value != float:
            raise AttributeError("The transaction_fee_base_price has to be a int value!")

    @property
    def transaction_fee_limit(self):
        return self.__transaction_fee_limit

    @transaction_fee_limit.setter
    def transaction_fee_limit(self, value: float):
        self.__transaction_fee_limit = value
        if value != float:
            raise AttributeError("The transaction_fee_limit has to be a int value!")
    
    @property
    def block_id(self):
        return self.__block_id

    @block_id.setter
    def block_id(self, value: bytes):
        self.__block_id = value
        if not isinstance(value, bytes):
            raise AttributeError("The block_id has to be in bytes format!")
        
    @property
    def tx_id(self):
        return self.__tx_id

    @tx_id.setter
    def tx_id(self, value: bytes):
        self.__tx_id = value
        if value != bytes:
            raise AttributeError("The tx_id has to be in bytes format!")
