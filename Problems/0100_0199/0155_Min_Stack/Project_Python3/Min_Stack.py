import sys

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = sys.maxsize
        self.head = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x < self.min:
            self.min = x
        
        self.node = Node(self.min)
        self.node.next = Node(x)

        if self.head == None or self.head.next == None:
            self.head = self.node
        else:
            temp = self.head
            self.head = self.node
            self.head.next.next = temp

    def pop(self):
        """
        :rtype: void
        """
        if self.head == None:
            dummy = 0
        else:
            currHead = self.head.next
            if currHead.next != None:
                self.head = currHead.next
                self.min = self.head.data
            else:
                self.head = None
                self.min = sys.maxsize

    def top(self):
        """
        :rtype: int
        """
        if self.head != None:
            return self.head.next.data
        else:
            return 0

    def getMin(self):
        """
        :rtype: int
        """
        return self.min

def calc():
    minStack = MinStack()

    minStack.push(-2)
    print("push(-2)")

    minStack.push(0)
    print("push(0)")

    minStack.push(-3)
    print("push(-3)")

    result = minStack.getMin()
    print("getMin() => {0}".format(result))

    minStack.pop()
    print("pop()")

    result = minStack.top()
    print("top() => {0}".format(result))

    result = minStack.getMin()
    print("getMin() => {0}".format(result))

def main():
    calc()

if __name__ == "__main__":
    main()
