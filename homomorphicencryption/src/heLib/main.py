# ********************************************************************************
# Copyright (c) 2024 Contributors to the Eclipse Foundation
# Copyright (c) 2024 German Aerospace Center (DLR e.V.)
#
# See the NOTICE file(s) distributed with this work for additional
# information regarding copyright ownership.
#
# This program and the accompanying materials are made available under the
# terms of the Apache License, Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# ********************************************************************************


import random
import seal
from seal import EncryptionParameters, SEALContext, KeyGenerator, IntegerEncoder, Encryptor, Decryptor, Evaluator

class simpleHE:
    def __init__(self, key_length=16):
        self.key_length = key_length
        self.public_key, self.private_key = self.generate_keys()

    def generate_keys(self):
        # Generate a simple random key
        private_key = random.randint(1, 2**self.key_length)
        public_key = private_key * 2  # Simple method to generate public key
        return public_key, private_key

    def encrypt(self, message):
        # Encrypt message by adding the public key
        noise = random.randint(1, 2**self.key_length)
        ciphertext = message + self.public_key + noise
        return ciphertext

    def decrypt(self, ciphertext):
        # Decrypt message by subtracting the private key
        original_message = (ciphertext - self.public_key) % self.private_key
        return original_message

    def add(self, ciphertext1, ciphertext2):
        # Homomorphic addition
        return ciphertext1 + ciphertext2

class FHE:
    def __init__(self, poly_modulus_degree=4096, plain_modulus_value=4096):
        # Setup encryption parameters
        self.parms = EncryptionParameters(seal.scheme_type.BFV)
        self.parms.set_poly_modulus_degree(poly_modulus_degree)
        self.parms.set_coeff_modulus(seal.CoeffModulus.BFVDefault(poly_modulus_degree))
        self.parms.set_plain_modulus(seal.PlainModulus.Batching(plain_modulus_value, 20))

        # Create SEALContext
        self.context = SEALContext(self.parms)

        # Key generation
        self.keygen = KeyGenerator(self.context)
        self.public_key = self.keygen.public_key()
        self.secret_key = self.keygen.secret_key()
        self.relin_keys = self.keygen.relin_keys()

        # Setup Encryptor, Decryptor, Evaluator, and Encoder
        self.encryptor = Encryptor(self.context, self.public_key)
        self.decryptor = Decryptor(self.context, self.secret_key)
        self.evaluator = Evaluator(self.context)
        self.encoder = IntegerEncoder(self.context)

    def encrypt(self, number):
        plain = self.encoder.encode(number)
        cipher = self.encryptor.encrypt(plain)
        return cipher

    def decrypt(self, cipher):
        plain = self.decryptor.decrypt(cipher)
        decoded = self.encoder.decode_int32(plain)
        return decoded

    def add(self, cipher1, cipher2):
        cipher_result = self.evaluator.add(cipher1, cipher2)
        return cipher_result
    
    def subtract(self, cipher1, cipher2):
        cipher_result = self.evaluator.sub(cipher1, cipher2)
        return cipher_result

    def multiply(self, cipher1, cipher2):
        cipher_result = self.evaluator.multiply(cipher1, cipher2)
        self.evaluator.relinearize_inplace(cipher_result, self.relin_keys)
        return cipher_result

    def relinearize(self, cipher):
        self.evaluator.relinearize_inplace(cipher, self.relin_keys)
        return cipher