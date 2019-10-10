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
                    print("stack not found... %s" %cmds[i])
                    exit(1)
                elif cmds[i] == "push":
                    stack.push(args[i])
                    print("Exec ... push(%d)" %args[i])
                elif cmds[i] == "peek":
                    result = stack.peek()
                    print("peek() .. %d" %result)
                elif cmds[i] == "pop":
                    result = stack.pop()
                    print("pop() ... %d" %result)
                elif cmds[i] == "empty":
                    result = stack.empty()
                    print("empty() ... %s" %result)
                else:
                    print("error... %s" %cmds[i])
                    exit(1)

def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
        print("Usage: python %s <testdata.txt>" %(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("%s not found..." %argv[1])
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        temp = temp.strip()
        if temp == "":
            continue
        print("argv[1] = %s" %temp)
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

    print("cmds[] = %s" %cmds)
    print("args[] = %s" %args)

    time0 = time.time()

    sl = Solution()
    result = sl.calc(cmds, args)

    time1 = time.time()

    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
