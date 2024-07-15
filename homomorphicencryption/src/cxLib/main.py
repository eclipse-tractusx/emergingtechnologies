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

from transitions import Machine
import requests
import time

class CatenaXClient:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
    
    def get_data(self, endpoint):
        response = requests.get(f'{self.base_url}/{endpoint}', headers=self.headers)
        return response.json()

    def post_data(self, endpoint, data):
        response = requests.post(f'{self.base_url}/{endpoint}', headers=self.headers, json=data)
        return response.json()


class CxConnection:
    states = ['initial', 'connecting', 'authenticating', 'connected', 'connection_failed']

    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        self.machine = Machine(model=self, states=ConnectionStateMachine.states, initial='initial')

        self.machine.add_transition(trigger='start_connection', source='initial', dest='connecting', before='connect')
        self.machine.add_transition(trigger='authenticate', source='connecting', dest='authenticating', before='authenticate')
        self.machine.add_transition(trigger='connection_success', source='authenticating', dest='connected')
        self.machine.add_transition(trigger='connection_failure', source=['connecting', 'authenticating'], dest='connection_failed')
        self.machine.add_transition(trigger='retry_connection', source='connection_failed', dest='connecting', before='connect')

    def connect(self):
        print("Connecting to the API...")
        try:
            response = requests.get(f'{self.base_url}/status', headers=self.headers)
            if response.status_code == 200:
                self.authenticate()
            else:
                self.connection_failure()
        except requests.RequestException:
            self.connection_failure()

    def authenticate(self):
        print("Authenticating...")
        try:
            response = requests.post(f'{self.base_url}/auth', headers=self.headers)
            if response.status_code == 200:
                self.connection_success()
            else:
                self.connection_failure()
        except requests.RequestException:
            self.connection_failure()

    def connection_success(self):
        print("Connection successful!")

    def connection_failure(self):
        print("Connection failed! Retrying in 5 seconds...")
        time.sleep(5)
        self.retry_connection()
