class Stack:

    def __init__(self):
        self.st = [] 
        self.tos = 0 

    def Push(self,x:int):
        self.st.append(x)
        self.tos += 1 

    def Top(self):
        return self.st[self.tos-1]

    def Empty(self):
        if self.tos == 0:
            return 1 
        else:
            return 0 

    def Pop(self):
        if self.Empty == 1:
            return "uderflow"
        else:
            x = self.st.pop(self.tos-1)
            self.tos -= 1 
            return x

def main():
    stack = Stack() 
    stack.Push(10)
    stack.Push(20) 
    stack.Push(30)
    print(stack.Pop())
    print(stack.Top()) 
    print(stack.Empty())
    print(stack.st)

if __name__ == "__main__":
    main()
