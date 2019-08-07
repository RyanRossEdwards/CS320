import sys
# import pandas as pd
# import numpy as np

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

# print(full_input, '\n')

# Turn the inputs into 2D arrays
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

# Reminder: [Row no./ Height] [Length]   //  [height,length]

class GridGraph:

    class Node:
        def __init__(self, weight, location, dimensions):
            self.weight = weight
            self.dv = -1
            self.location = location
            self.dimensions = dimensions
            self.connections = []

            # Populates the directed connections in a 'grid' formation looks like -> [X]
            for i in range(self.location[0]-1, self.location[0]+2): # Plus 2 to account for range => [first, last)
                for j in range(self.location[1]-1, self.location[1]+2):
                    if not (i < 0 or j < 0 or i >= self.dimensions[0] or j >= self.dimensions[1] or ([i,j] == self.location)):
                        self.connections += [[i, j]]
            
        def get_weight(self):
            return self.weight

        def get_dv(self):
            return self.dv

        def set_dv(self, dv):
            # Debugging
            # print('THE DV', self.location, dv)

            self.dv = dv

        def get_location(self):
            return self.location

        def get_connections(self):
            return self.connections



    def __init__(self, dimensions, nodes):
        self.dimensions = dimensions
        self.nodes = []

        # Should compute OK despite O(n^4)
        # As max is 400x400x3x3 ~ 1.5 million
        for i in range(self.dimensions[0]):
            row = []
            for j in range(self.dimensions[1]):
                row += [self.Node(nodes[i][j], [i,j], self.dimensions)]
            self.nodes += [row]

    def get_dimensions(self):
        return self.dimensions

    def get_nodes(self):
        return self.nodes

    def node(self, location):
        return self.nodes[location[0]][location[1]]



def dijkstra_algorithm (graph):
    explored_nodes = [] # Stores location array not object
    committed_nodes = []
    
    start = [graph.get_dimensions()[0]-1, 0] # Start = [Max, 0]
    graph.node(start).set_dv(graph.node(start).get_weight())
    final = [0, graph.get_dimensions()[1]-1] # Final = [0, Max]
    explored_nodes += [start]


    # while final not in explored_nodes:
    while not explored_nodes == []:
        unexplored_nodes = []

        for i in range(len(explored_nodes)):
            if explored_nodes[i] not in committed_nodes:
                current_node = graph.node(explored_nodes[i])
                for node_location in current_node.get_connections():
                    # print('XXX - CURRENT NODE CONNECTIONS ======', node_location)
                    if node_location not in committed_nodes:
                        unexplored_nodes += [[node_location, current_node.get_location()]]

        # print('UNEXPLORED NODES', unexplored_nodes)
        
        # print('PRECOMMIT', committed_nodes)
        committed_nodes += explored_nodes
        # print('COMMIT', committed_nodes)
        # print(final not in explored_nodes)
        explored_nodes = [] # Empty the explored nodes

        for j in range(len(unexplored_nodes)-1,-1,-1):
            current_node_a = graph.node(unexplored_nodes[j][0])
            current_node_b = graph.node(unexplored_nodes[j][1]) #this is the one connected with it
            test_dv = current_node_a.get_weight() + current_node_b.get_dv()
            # print('PRE-DV', current_node_a.get_location(), current_node_b.get_location(), test_dv, '===', current_node_a.get_weight(), current_node_b.get_dv())
            # print('moment-of-truth', current_node_a.get_weight(), current_node_b.get_dv())
            if (current_node_a.get_dv() == -1) or (current_node_a.get_dv() > test_dv):
                current_node_a.set_dv(test_dv)

            explored_nodes += [unexplored_nodes[j][0]]


    # print(graph.node(start).get_weight())
    # print(explored_nodes)

    # Change to return!
    print(graph.node(final).get_dv())

    # while graph.get_node_count() < len(explored_nodes):




# Test Cases

# my_graph = GridGraph([2,2],[[0,1],[2,3]])
# my_graph = GridGraph([3,3],[[0,6,2],[1,8,4],[2,3,7]])
# my_graph = GridGraph( [3,5],[[1,3,9,9,1],[5,10,1,8,4],[2,7,8,2,6]])
# print(my_graph.get_nodes())

# dijkstra_algorithm(my_graph)


# For final implementation need to use stdio for what gets returned above!!

for grid in grids:
    dijkstra_algorithm(GridGraph(grid[0],grid[1]))





# [
#     [[0, 0], [1, 0]],   # -> 3 + 0 = 3
# [[0, 1], [1, 0]], 
# [[2, 0], [1, 0]], 
#     [[0, 0], [1, 1]],   # -> 10 + 0 = 10
# [[0, 1], [1, 1]], 
# [[0, 2], [1, 1]], 
# [[1, 2], [1, 1]], 
# [[2, 0], [1, 1]], 
# [[2, 2], [1, 1]], 
# [[1, 2], [2, 1]], 
# [[2, 0], [2, 1]], 
# [[2, 2], [2, 1]]]

# COMMIT [[2, 0], [1, 0], [1, 1], [2, 1]]

# THE DV [0, 0] 1
# THE DV [0, 1] 7
# THE DV [0, 2] 10
# THE DV [1, 2] 12
# THE DV [2, 2] 15
# THE DV [1, 2] 7
# THE DV [2, 2] 10

























