#Write A Program  to implement stack operations
#############  STACK IMPLEMENTATION  ###############
"""
    Stack:implemented as a list
    top:integer having position of topmost element in Stack
"""
def isEmpty(stk):
    if stk==[]:
        return True
    else:
        return False
def Push(stk):
    global top
    item=int(input("Enter item:"))
    stk.append(item)
    top=len(stk)-1
def Pop(stk):
    global top
    if isEmpty(stk):
        print("\nUnderflow! Stack is empty!")
    else:
        item=stk.pop()
        if len(stk)==0:
            top=None
        else:
            top=len(stk)-1
        print("\nPopped item is",item)
def Peek(stk):
    if isEmpty(stk):
        print("\nUnderflow! Stack is empty!")
    else:
        top=len(stk)-1
        print("\nTopmost item is",stk[top])
def Display(stk):
    if isEmpty(stk):
        print("\nStack empty")
    else:
        top=len(stk)-1
        print("\n",stk[top],"<-top")
        for a in range(top-1,-1,-1):
            print(stk[a])
Stack=[]
top=None
while True:
    print("\nSTACK OPERATIONS")
    print("1.Push")
    print("2.Pop")
    print("3.Peek")
    print("4.Display")
    print("5.Exit")
    ch=int(input("Enter your choice(1-5):"))
    if ch==1:
        Push(Stack)
    elif ch==2:
        Pop(Stack)
    elif ch==3:
        Peek(Stack)
    elif ch==4:
        Display(Stack)
    elif ch==5:
        print("Successfully Exited!")
        break
    else:
        print("\nInvalid choice!") 