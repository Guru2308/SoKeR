class Stack:

    def __init__ (self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack)-1]
    
st = Stack()
st.push(1)
st.push(7)
st.push(4)
st.pop()
print(st.peek())