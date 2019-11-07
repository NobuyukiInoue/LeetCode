# coding: utf-8

import copy
import os
import sys
import time

class Solution:
#   def evalRPN(self, tokens: List[str]) -> int:
    def evalRPN(self, tokens):
        # 60ms
        stack = []
        for ch in tokens:
            if ch == '+':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a + b)
            elif ch == '-':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a - b)
            elif ch == '*':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a * b)
            elif ch == '/':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a / b)
            else:
                stack.append(ch)
        return int(stack[0])

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
        print("args = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    tokens = temp.replace(" ","").replace("\"","").replace("[","").replace("]","").rstrip().split(",")
    print("tokens = {0}".format(tokens))
    time0 = time.time()

    sl = Solution()
    result = sl.evalRPN(tokens)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
