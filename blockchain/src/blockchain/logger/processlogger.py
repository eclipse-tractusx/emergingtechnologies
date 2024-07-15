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


import logging


class ProcessLogger:
    """
    ProcessLogger is a custom logging utility class designed to facilitate structured
    and standardized logging for various processes within an application.

    Attributes:
        name (str): The name of the logger, typically indicating the context or
                    component using this logger.
        logger (logging.Logger): The underlying logger instance from the logging module.
        stream_handler (logging.StreamHandler): The handler responsible for outputting
                                                log messages to the console or stream.
        formatter (logging.Formatter): The formatter that defines the log message format.
    """
    
    def __init__(self, name) -> None:
        self.name = name
        self.logger = logging.getLogger(f"ProcessLogger.{self.name}")
        self.stream_handler = logging.StreamHandler() 
        self.formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
        
        self.logger.setLevel(logging.DEBUG)
        
        # set adjustment for process info handler
        #self.stream_handler.setLevel(logging.INFO)
        self.stream_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.stream_handler)
        
    def  log_info(self, message):
        self.logger.info(f"{message}")
    
    def log_debug(self, message):
        self.logger.debug(f"{message}")
        