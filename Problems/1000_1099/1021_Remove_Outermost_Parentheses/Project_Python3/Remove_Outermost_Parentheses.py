import math
import os
import collections
import sys
import time
from functools import reduce

class Solution:
#   def removeOuterParentheses(self, S: str) -> str:
    def removeOuterParentheses(self, S):
        # 40ms
        res, opened = [], 0
        for c in S:
            if c == '(' and opened > 0:
                res.append(c)
            if c == ')' and opened > 1:
                res.append(c)
            if c == '(':
                opened += 1
            else:
                opened -= 1
        return "".join(res)

    def removeOuterParentheses2(self, S):
        # 1552ms
        stack = 0
        pos = []
        for i in range(len(S)):
            if S[i] == "(":
                if stack == 0:
                    pos.append(i)
                stack += 1
            if S[i] == ")":
                if stack == 1:
                    pos.append(i)
                stack -= 1
        result = ""
        for i in range(len(S)):
            if not i in pos:
                result += S[i]
        return result

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
    S = temp.replace(", ",",").replace("\"","").replace("[","").replace("]","").rstrip()
    print("s = {0}".format(S))

    sl = Solution()
    time0 = time.time()

    result = sl.removeOuterParentheses(S)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
