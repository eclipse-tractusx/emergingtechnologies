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

from streamlit_agraph import agraph, Node, Edge, Config

graph = None

def add():
    global graph
    nodes = []
    edges = []
    nodes.append( Node(id="p0", 
                    label="Player 0", 
                    size=25,
                    ) 
                ) # includes **kwargs
    nodes.append( Node(id="p1", 
                    label="Player 1",
                    size=25,
                    ) 
                )
    edges.append( Edge(source="p0", 
                    label="connected", 
                    target="p1", 
                    # **kwargs
                    ) 
                ) 

    config = Config(width=750,
                    height=300,
                    directed=False, 
                    physics=True, 
                    hierarchical=False,
                    # **kwargs
                    )

    graph = agraph(nodes=nodes, 
                    edges=edges, 
                    config=config)