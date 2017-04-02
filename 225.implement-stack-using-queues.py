import collections


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.data.append(x)
        for i in range(0, len(self.data) - 1):
            self.data.append(self.data.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.data.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.data[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.data) == 0


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.pop())
obj.push(4)
print(obj.pop())
print(obj.pop())
