#Write A Program  to implement a stack for these book-details(bookno,book name).
#That is,now each item node of the stack contains two types of information-a bookno and its name
#Just implement Push and display operations.
"""
    Stack:implemented as a list
    top:integer having position of topmost element in Stack
"""
def cls():
    print("\n"*5)
def isEmpty(stk):
    if stk==[]:
        return True
    else:
        return False
def Push(stk):
    global top
    bno=int(input("Enter Book no. to be inserted:"))
    bname=input("Enter Book name to be inserted:")
    stk.append([bno,bname])
    top=len(stk)-1
def Display(stk):
    if isEmpty(stk):
        print("\nStack empty")
    else:
        top=len(stk)-1
        print("\n",stk[top],"<-top")
        for a in range(top-1,-1,-1):
            print(stk[a])
#_main_
Stack=[]
top=None
while True:
    cls()
    print("STACK OPERATIONS")
    print("1.Push")
    print("2.Display")
    print("3.Exit")
    ch=int(input("Enter your choice(1-3):"))
    if ch==1:
        Push(Stack)
        input("Press Enter to continue...")
    elif ch==2:
        Display(Stack)
        input("Press Enter to continue...")
    elif ch==3:
        print("Successfully Exited!")
        break
    else:
        print("\nInvalid choice!")
        input("Press Enter to continue...")