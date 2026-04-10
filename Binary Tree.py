# Binary tree 
# -it has atmost 2 child
# -includes 0 ,1, 2

# Full Binary tree 
# -each node has either 0 or 2 children
# -no node has single child

# Complete Binary tree
# all levels excpet possibly the last are completely fileed
# nodes in last level are filled from left to right  

# Perfect Binary tree
# - all internal nodes have exactly two nodes 
# - all leaf nodes are at same level

#Operations on Tree
# - Creation
# - insertion
# - deletion

# class Tree:
#     def __init__(self,data):
#         self.data=data
#         self.children=[]

#     def addChild(self,child):
#         self.children.append(child)

#     def __str__(self,level=0):
#         ret=" "* level+str(self.data)+"\n"
#         for child in self.children:
#             ret+=child.__str__(level+1)
#         return ret

# obj=Tree("N1")
# n2=Tree("N2")
# n3=Tree("N3")
# n4=Tree("N4")
# n5=Tree("N5")
# n6=Tree("N6")
# n7=Tree("N7")
# n9=Tree("N9")
# n10=Tree("N10")

# obj.addChild(n2)
# obj.addChild(n3)
# n2.addChild(n4)
# n2.addChild(n5)
# n4.addChild(n9)
# n4.addChild(n10)
# n3.addChild(n6)
# n3.addChild(n7)

# print(obj)

class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self):
        self.root=None

    def insert(self,value):
        if self.root is None:
            self.root=Node(value)
        else:
            self.insertNode(self.root,value)

    def insertNode(self,rootNode,value):
        if value<rootNode.value:
            if rootNode.left is None:
                rootNode.left=Node(value)
            else:
                self.insertNode(rootNode.left,value)
        else:
            if rootNode.right is None:
                rootNode.right=Node(value)
            else:
                self.insertNode(rootNode.left,value)
btObj=BinaryTree()
btObj.insert(50)
btObj.insert(30)
btObj.insert(70)
print(btObj)

