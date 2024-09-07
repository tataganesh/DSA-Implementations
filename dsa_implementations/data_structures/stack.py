class Stack:
    def __init__(self):
        self.array = []

    def push(self, x):
        """Push element into stack"""
        self.array.append(x)

    def pop(self):
        """Pop last inserted element from stack"""
        if not self.array:
            raise IndexError("Cannot pop from empty stack")
        return self.array.pop()

    def top(self):
        """Get top (last inserted) element in stack"""
        if not self.array:
            raise IndexError("Cannot retrieve top element from empty stack")
        return self.array[-1]

    def size(self):
        """Get size of stack"""
        return len(self.array)

    def isEmpty(self):
        """Check if stack is empty"""
        return not self.array


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    print(f"Top Element: {s.top()}")  # Prints 1
    print(f"Popped Element: {s.pop()}")  # Pops 1
    s.top()  # Raises exception
