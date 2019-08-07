"""
COMPSCI 320 - Assignment 1
Ryan Edwards
"""

# BSD 3-Clause License

# Copyright (c) 2019, Ryan Edwards
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.

# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.

# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import sys

# Can test with $ python a1.py < input

# Capture stdin
full_input = []

for line in sys.stdin:
    try:
        array = ([int(x) for x in line.split()])
        full_input += [array]
        if array == [0,0]:
            break
    except:
        continue

# Turn the inputs into multi-dimensional arrays
# Reminder: [Row no./ Height] [Length]   //  [height,length]
grids = []
new_grid = True

for i in range(len(full_input)-1):
    if new_grid:
        new_grid = False
        dimensions = full_input[i]
        dimension_total = i + dimensions[0]
        grid_to_add = [dimensions, []]
    
    elif not new_grid and i < dimension_total:
        grid_to_add[1] += [full_input[i]]

    else:
        new_grid = True
        grid_to_add[1] += [full_input[i]]
        grids += [grid_to_add]
        continue


class GridGraph:

    class Node:
        def __init__(self, weight, location, dimensions):
            self.weight = weight
            self.location = location
            self.connections = []
            self.dist = float('inf') # Python is nice and makes ints and floats compareable

            # Populates the directed connections in a 'grid' formation looks like -> [X]
            # Because it just uses coordinates for where the values will be saved,
            # it only needs to be iterated once as the Node object doesn't need to exist yet.

            for i in range(self.location[0]-1, self.location[0]+2): # Plus 2 to account for range => [first, last)
                for j in range(self.location[1]-1, self.location[1]+2):
                    if not (i < 0 or j < 0 or i >= dimensions[0] or j >= dimensions[1] or ([i,j] == self.location)):
                        self.connections += [[i, j]]

    def __init__(self, dimensions, nodes):
        self.dimensions = dimensions
        self.nodes = []
        
        self.all_nodes = []

        # Should compute OK despite O(n^4)
        # As max is 400x400x3x3 ~ 1.5 million
        for i in range(self.dimensions[0]):
            row = []
            for j in range(self.dimensions[1]):
                new_node = self.Node(nodes[i][j], [i,j], self.dimensions)
                row += [new_node]
                self.all_nodes += [new_node]
            self.nodes += [row]

    def node(self, location):
        return self.nodes[location[0]][location[1]]



def dijkstra(graph):
    
    all_nodes = graph.all_nodes

    source = graph.node([graph.dimensions[0]-1, 0])
    source.dist = source.weight

    while not all_nodes == []:
        u = all_nodes[0]
        u_index = 0
        for i in range(len(all_nodes)):
            if all_nodes[i].dist < u.dist:
                u = all_nodes[i]
                u_index = i
        all_nodes.pop(u_index)

        for neighbour_pointer in u.connections:
            # Using pointers as this greatly reduces required iterations
            neighbour = graph.node(neighbour_pointer)
            if neighbour in all_nodes:
                alt = u.dist + neighbour.weight
                if alt < neighbour.dist:
                    neighbour.dist = alt

    return graph.node([0, graph.dimensions[1]-1]).dist



for grid in grids:
    print(dijkstra(GridGraph(grid[0],grid[1])))


# Test Cases

# my_graph = GridGraph([2,2],[[0,1],[2,3]])
# my_graph = GridGraph([3,3],[[0,6,2],[1,8,4],[2,3,7]])
# my_graph = GridGraph( [3,5],[[1,3,9,9,1],[5,10,1,8,4],[2,7,8,2,6]])

# print(dijkstra(my_graph))












































