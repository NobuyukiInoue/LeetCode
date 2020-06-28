import os
import sys
import time

class MyStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.inStack, self.outStack = [], []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.inStack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.move()
        return self.outStack.pop()

    def peek(self):
        """
        :rtype: int
        """
        self.move()
        return self.outStack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return (not self.inStack) and (not self.outStack) 
        
    def move(self):
        """
        :rtype nothing
        """
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

class Solution:
    def calc(self, cmds, args):
        for i in range(len(cmds)):
            if cmds[i] == "MyQueue":
                stack = MyStack()
                print("Exec MyStack()")
            else:
                if stack == None:
                    print("stack not found... {0}".format(cmds[i]))
                    exit(1)
                elif cmds[i] == "push":
                    stack.push(args[i])
                    print("Exec ... push({0:d})".format(args[i]))
                elif cmds[i] == "peek":
                    result = stack.peek()
                    print("peek() .. {0:d}".format(result))
                elif cmds[i] == "pop":
                    result = stack.pop()
                    print("pop() ... {0:d}".format(result))
                elif cmds[i] == "empty":
                    result = stack.empty()
                    print("empty() ... {0}".format(result))
                else:
                    print("error... {0}".format(cmds[i]))
                    exit(1)

def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
        print("Usage: python {0} <testdata.txt>".format(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("{0} not found...".format(argv[1]))
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        temp = temp.strip()
        if temp == "":
            continue
        print("argv[1] = {0}".format(temp))
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],]")
    cmds = flds[0].split(",")
    args_str = flds[1].replace("[","").replace("]","").split(",")
    args = [0]*len(args_str)
    for i in range(len(args_str)):
        if args_str[i] == '':
            args[i] = 0
        else:
            args[i] = int(args_str[i])

    print("cmds[] = {0}".format(cmds))
    print("args[] = {0}".format(args))

    sl = Solution()
    time0 = time.time()
    result = sl.calc(cmds, args)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
