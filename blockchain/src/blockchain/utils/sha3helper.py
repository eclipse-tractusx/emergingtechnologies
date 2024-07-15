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


import binascii
import pickle
import hashlib


class SHA3Helper:
    """
    SHA3Helper is a auxilary class to encode strings to byte arrays.
    """
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def hash256_as_hex(obj: object) -> str:
        """
        Converts an object hash to string.
        """
        return binascii.hexlify(SHA3Helper.hash256(obj)).decode('utf-8')

    @staticmethod
    def digest_to_hex(digest: bytes) -> str: #* to use it for multiple recievers -> change to a list of bytearrays
        """
        Converts a bytearray to string.
        """
        return binascii.hexlify(digest).decode('utf-8')
    
    @staticmethod
    def hash256(obj: object) -> bytes:
        try:
            # Serialize the object using pickle
            data = pickle.dumps(obj, protocol=pickle.HIGHEST_PROTOCOL)

            # Compute the SHA-256 hash of the serialized data
            hash_obj = hashlib.sha256(data)

            # Return the hash value as a byte array
            return hash_obj.digest()
            
        except pickle.PickleError as e:
            print(f"Error serializing object: {e}")
