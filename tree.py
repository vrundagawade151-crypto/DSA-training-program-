# class Tree:
#     def __init__(self,data):
#         self.data=data #instance variable(create sepeerate memory for each object)
#         self.children=[]

#     def addChild(self,child):
#         self.children.append(child)  #object creation

#     def __str__(self,level=0):
#         ret=" "* level+str(self.data)+"\n"
#         for child in self.children:
#             ret+=child.__str__(level+1)
#         return ret

# rootNode=Tree("Drinks")
# hot=Tree("Hot")
# cold=Tree("Cold")
# tea=Tree("Tea")
# coffee=Tree("Coffee")
# alcoholic=Tree("Alcoholic")
# nonalcoholic=Tree("NonAlcoholic")

# rootNode.addChild(hot)
# rootNode.addChild(cold)
# hot.addChild(tea)
# hot.addChild(coffee)
# cold.addChild(alcoholic)
# cold.addChild(nonalcoholic)

# print(rootNode)

