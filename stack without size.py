import sys
class Stack:
    def __init__(self):
        self.stackList=[] #stack created
    
    def push(self,value):
        self.stackList.append(value)
    
    def display(self):
        print("---------------------")
        print(self.stackList)
        print("---------------------")

    def isEmpty(self):
        if self.stackList==[]:
            return True
        else:
            return False
        
    def stackPop(self):
        if self.isEmpty():
            print("---------------------")
            print("Stack is empty")
            print("---------------------")
        else:
            self.stackList.pop()

    def deleteStack(self):
        self.stackList=None
        print("---------------------")
        return "Stack is deleted"
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.stackList[-1]

        

stackObj=Stack()
while True:
    print("*****************    Stack   *****************")
    print("1.Push elements in Stack")
    print("2.Display elements in Stack")
    print("3.Check isEmpty")
    print("4.Remove elements from stack")
    print("5.Delete Stack")
    # print("")
    choice=int(input("Enter your choice : "))
    if choice==1:
        print("---------------------------------")
        val=int(input("Enter the value for stack : "))
        print("---------------------------------")
        stackObj.push(val)
    elif choice==2:
        stackObj.display()
    elif choice==3:
        print("---------------------")
        print(stackObj.isEmpty())
        print("---------------------")
    elif choice==4:
        print("Popped element is : ",stackObj.stackList[-1])
        stackObj.stackPop()
    elif choice==5:
        stackObj.deleteStack()
    elif choice==6:
        stackObj.peek()
    elif choice==7:
        sys.exit()
        