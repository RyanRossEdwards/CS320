"""
COMPSCI 320 - Assignment 1
Ryan Edwards
"""

import sys
from heapq import heappush, heappop, heapify

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

            # This is max 9 iterations
            for i in range(self.location[0]-1, self.location[0]+2): # Plus 2 to account for range => [first, last)
                for j in range(self.location[1]-1, self.location[1]+2):
                    if not (i < 0 or j < 0 or i >= dimensions[0] or j >= dimensions[1] or ([i,j] == self.location)):
                        self.connections += [[i, j]]

        # Needed for heappush (allows objects to be compared)
        def __lt__(self, other):
            return self.dist < other.dist


    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.nodes = []
        self.all_nodes = []

    def add_row(self, row_input, row_number):
        row = []
        for j in range(self.dimensions[1]):
            new_node = self.Node(row_input[j], [row_number,j], self.dimensions)
            row += [new_node]
        self.nodes += [row]

    def node(self, location):
        return self.nodes[location[0]][location[1]]


def dijkstra(graph):
    
    all_nodes = graph.all_nodes

    source = graph.node([graph.dimensions[0]-1, 0])
    source.dist = source.weight
    heappush(all_nodes, source)

    while not all_nodes == []:
        # Get the node with the smallest distance
        u = heappop(all_nodes)
        graph.all_nodes = []

        for neighbour_pointer in u.connections: # max 9 iterations
            # Using pointers as this greatly reduces required iterations
            neighbour = graph.node(neighbour_pointer)
            
            alt = u.dist + neighbour.weight
            if alt < neighbour.dist:
                neighbour.dist = alt
                heappush(all_nodes, neighbour)


    return graph.node([0, graph.dimensions[1]-1]).dist


# Capture stdin
# Reminder: [Row no./ Height] [Length]   //  [height,length]
new_grid = True

for line in sys.stdin:
    array = ([int(x) for x in line.split()])
    
    if array == [0,0]:
        break

    if new_grid:
        new_grid = False
        dimensions = array
        dimension_counter = 0
        my_gridgraph = GridGraph(dimensions)
    
    elif not new_grid and dimension_counter < dimensions[0]-1:
        my_gridgraph.add_row(array, dimension_counter)
        dimension_counter += 1

    else:
        new_grid = True
        my_gridgraph.add_row(array, dimension_counter)
        print(dijkstra(my_gridgraph))