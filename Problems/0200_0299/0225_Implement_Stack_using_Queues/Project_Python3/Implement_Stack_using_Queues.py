import os
import sys
import time

class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.data.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        res = self.data[-1]
        self.data.pop()
        return res

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.data[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.data) == 0

class Solution:
    def calc(self, cmds, args):
        for i in range(len(cmds)):
            if cmds[i] == "MyStack":
                stack = MyStack()
                print("Execute MyStack()")
            else:
                if stack == None:
                    print("stack not found... {0}".format(cmds[i]))
                    exit(1)
                elif cmds[i] == "push":
                    stack.push(args[i])
                    print("Execute push({0:d})".format(args[i]))
                elif cmds[i] == "top":
                    result = stack.top()
                    print("top() ==> {0:d}".format(result))
                elif cmds[i] == "pop":
                    result = stack.pop()
                    print("pop() ==> {0:d}".format(result))
                elif cmds[i] == "empty":
                    result = stack.empty()
                    print("empty() ==> {0}".format(result))
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
        print("args = {0}".format(temp))
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    flds = temp.replace(" ","").replace("\"","").rstrip().split("],[[")
    cmds = flds[0].replace("[[","").split(",")
    args_str = flds[1].replace("[","").replace("]","").split(",")
    args = [0]*len(args_str)
    for i in range(len(args_str)):
        if args_str[i] == '':
            args[i] = 0
        else:
            args[i] = int(args_str[i])

    print("cmds[] = {0}",format(cmds))
    print("args[] = {0}".format(args))

    sl = Solution()
    time0 = time.time()

    result = sl.calc(cmds, args)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
