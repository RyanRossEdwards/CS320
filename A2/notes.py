class Node:
    def __init__(self,x,y,left,right):
        self.x = x
        self.y = y
        self.left = left
        self.right = right

class XSorted:
    def __init__(self,)



## Might want a tree structure to sort the nodes

# Maybe not

class Node:
    def __init__(self,x,y,left,right):
        self.x = x
        self.y = y
        self.left = left
        self.right = right

# This keeps adding nodes to the end of a list with pointers
class List:
    def __init__(self,x,y):
        self.first = Node(x,y,None,None)
        self.last = self.first
        self.length = 1

    def add(self, x, y): 
        self.last.right = Node(x,y,self.last,None)
        self.last = self.last.right
        self.length += 1


# # This is a revised list for sorted x
# class XList:
#     def __init__(self, x, y):
#         self.first = Node(x,y,None,None)
#         self.last = self.first
#         self.length = 1

#     def add(self, x, y):




# Using HeapQ










