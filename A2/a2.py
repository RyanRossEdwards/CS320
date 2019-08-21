import sys
from math import ceil
import time

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

    # print(p_x_orig, p_y_orig, p_x, p_y)

    brute_start = time.time()
    a = brute(p_x_orig, p_x)
    brute_end = time.time()

    print('Brute Force Answer =', a, 'time =', brute_end - brute_start)

    dc_start = time.time()
    b = closest_pair(p_x_orig, p_y_orig, p_x, p_y, length)
    dc_end = time.time()
    
    print('DC Answer =', b, 'time =', dc_end - dc_start)

    # for i in range(len(p_x)):
    #     node = heappop(p_x)
    #     print(node.x, node.y)
    # for i in range(len(p_y)):
    #     node = heappop(p_y)
    #     print(node.x, node.y)


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


# Lazy programming - should merge functions once working!!
# Based on overall implementation, thous should cover both cases
# because it only fires at the end or if <=3 (so seven is fine)
def brute_seven(p_x_orig, p_x):
    p1 = p_x_orig[p_x[0][0]]
    p2 = p_x_orig[p_x[1][0]]
    delta = squared_euclidean_distance(p1, p2)

    length = len(p_x) #O(1) time, stored value, doesn't count
    # Could speed up by plugging length into this! (very minor)
    if length == 2:
        return delta

    for i in range(length - 1):
        
        # Prevent overflow and max 7
        my_max = i + 8
        if my_max > length:
            my_max = length

        for j in range(i + 1, my_max):
            if i != 0 and j != 1:
                delta_new = squared_euclidean_distance(p_x_orig[p_x[i][0]], p_x_orig[p_x[j][0]])
                if delta_new < delta:  # Update min_dist and points
                    delta = delta_new
    return delta


def closest_pair(p_x_orig, p_y_orig, p_x, p_y, length):

    # Note can revise - len() in python is O(1) -> doesn't 'count' each time
    # Keeping the length saved might reduce 'some' time though
    # print('length =', length, len(p_x))

    # Base Case:
    if length <= 3:
        return brute(p_x_orig, p_x)

    
    # Recursive Divide and Conquer Function begins:

    # Compute vertical line L
    # The middle node = l_median - 1
    median = ceil(length / 2)
    # print(p_x_orig[p_x[median]][0])

    try:
        l_median = p_x_orig[p_x[median]][0]
    except:
        print(p_x, 'median', median, 'length', length, len(p_x))
        return 0

    # add to U and V
    # save as index to avoid stack overflow
    # u_x = p_x[:l_median]
    # u_y = []
    # v_x = p_x [l_median:]
    # v_y = []

    u_x, u_y, v_x, v_y = [], [], [], []


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

    

    # print(u_x, v_x, u_y, v_y)


    delta_1 = closest_pair(p_x_orig, p_y_orig, u_x, u_y, median)
    delta_2 = closest_pair(p_x_orig, p_y_orig, v_x, v_y, length - median)
    delta = min(delta_1, delta_2)

    # Get the points within the 2 * delta strip

    # Following gets the range of delta and avoids out of bounds
    delta_min = median - delta - 1 # unsure about -1
    if delta_min < 0:
        delta_min = 0
    delta_max = median + delta
    if delta_max > length:
        delta_max = length

    s_x = []
    s_y = []

    # Gets points S in P within 2 * delta strip
    for i in range(delta_min, delta_max):
        s_x += [p_x[i]]

        # Gets sorted Y component
        y_index = p_x_orig[p_x[i]][1] # This is all the y values
        # print('yindex', y_index, 'pxi', p_x[i])
        s_y += [[p_x[i], y_index]] # This points to X
        # print(s_y)
        # Need to sort s_y based on y_index

    s_length = len(s_x) # don't need?
    
    s_y.sort(key= lambda k: k[1])  #Note this is ~ nlogn time, might need improvement

    return min(delta, brute_seven(p_x_orig, s_y))




main()