import sys
from math import ceil

class XNode:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Needed for heappush (allows objects to be compared)
    # XNode is sorted based on x
    def __lt__(self, other):
        return self.x < other.x

class YNode:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Needed for heappush (allows objects to be compared)
    # XNode is sorted based on x
    def __lt__(self, other):
        return self.y < other.y

# Make a container class that keeps the length so 'median' gets computed faster
# class Container:


def squared_euclidean_distance(coordinate1, coordinate2):
    return (coordinate1[0] - coordinate2[0]) ** 2 + (coordinate1[1] - coordinate2[1]) ** 2


def main():

    # Preprocessing step in O(nlogn)
    p_x_orig = []
    p_y_orig = []

    # Stores the index values
    p_x = []
    p_y = []

    length = 0

    for line in sys.stdin:
        array = ([int(x) for x in line.split()])
        p_x_orig += [array]
        p_y_orig += [array]
        p_x += [length]
        p_y += [length]
        length += 1

    p_x_orig.sort(key= lambda k: k[0])
    p_y_orig.sort(key= lambda k: k[1])

    print(p_x_orig, p_y_orig, p_x, p_y)

    print(brute(p_x_orig, p_x))

    # closest_pair(p_x_orig, p_y_orig, p_x, p_y, length)

    # for i in range(len(p_x)):
    #     node = heappop(p_x)
    #     print(node.x, node.y)
    # for i in range(len(p_y)):
    #     node = heappop(p_y)
    #     print(node.x, node.y)


# Note can revise - len() in python is O(1) -> doesn't 'count' each time

def brute(p_x_orig, p_x):
    p1 = p_x_orig[p_x[0]]
    p2 = p_x_orig[p_x[1]]
    delta = squared_euclidean_distance(p1, p2)

    length = len(p_x) #O(1) time, stored value, doesn't count
    if length == 2:
        return delta

    for i in range(length - 1):
        for j in range(i + 1, length):
            if i != 0 and j != 1:
                delta_new = squared_euclidean_distance(p_x_orig[p_x[i]], p_x_orig[p_x[j]])
                if delta_new < delta:  # Update min_dist and points
                    delta = delta_new
    return delta


def closest_pair(p_x_orig, p_y_orig, p_x, p_y, length):
    
    if length <= 3:
        return brute(p_x_orig, p_x)

    # Compute vertical line L
    # The middle node = l_median - 1

    median = ceil(length / 2)
    print(p_x_orig[p_x[median]][0])

    l_median = p_x_orig[p_x[median]][0]

    # add to U and V
    # save as index to avoid stack overflow
    u_x = []
    u_y = []
    v_x = []
    v_y = []

    # This can be sped up by splitting x
    # p_x[:l_median] and p_x [l_median:]
    
    for i in range(length):
        if p_x_orig[p_x[i]][0] < l_median:
            u_x += [p_x[i]]
        else:
            v_x += [p_x[i]]

        if p_y_orig[p_y[i]][0] < l_median:
            u_y += [p_y[i]]
        else:
            v_y += [p_y[i]]

    

    print(u_x, v_x, u_y, v_y)

    # print(squared_euclidean_distance([0,0],[2,2]))
    # print(squared_euclidean_distance([4,4],[2,2]))


    # Base Case
    # test for v_x == [], maybe v_y, return the 
    

    # if v_x == []:
    #     delta = 1000000

    # else:
    #     delta_1 = closest_pair(p_x_orig, p_y_orig, u_x, u_y, median)
    #     delta_2 = closest_pair(p_x_orig, p_y_orig, v_x, v_y, length - median)
    #     delta = min(delta_1, delta_2)

    #     2_delta_min = median - delta - 1 # unsure about -1
    #     if 2_delta_min < 0:
    #         2_delta_min = 0
    #     2_delta_max = median + delta
    #     if 2_delta_max > length:
    #         2_delta_max = length

    #     s_x = []
    #     s_y = []

    #     for i in range(2_delta_min, 2_delta_max):
    #         s_x += p_x[i]

    #         if s_x in p_y

    #     for yindex in p_y:
    #         for index in s_x:
    #             if p_y_orig[yindex] == p_x_orig[index]:



































main()