import sys
from heapq import heappush, heappop, heapify

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


def main():

    # Preprocessing step in O(nlogn)
    p_x = []
    p_y = []

    for line in sys.stdin:
        array = ([int(x) for x in line.split()])
        heappush(p_x, XNode(array[0], array[1]))
        heappush(p_y, YNode(array[0], array[1]))

    for i in range(len(p_x)):
        node = heappop(p_x)
        print(node.x, node.y)
    for i in range(len(p_y)):
        node = heappop(p_y)
        print(node.x, node.y)


main()