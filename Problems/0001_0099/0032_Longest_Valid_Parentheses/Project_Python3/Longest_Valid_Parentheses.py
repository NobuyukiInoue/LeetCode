import math
import os
import collections
import sys
import time
from functools import reduce

class Solution:
#   def longestValidParentheses(self, s: str) -> int:
    def longestValidParentheses(self, s):
        longest = brackets = min_brackets = 0
        m = [0] * len(s) 
        for token in s:
            if token == "(":
                brackets += 1
            else:
                brackets -= 1
                if brackets < min_brackets:
                    min_brackets = brackets
                else:
                    m[brackets] += 2 + m[brackets+1]
                    longest = max(m[brackets], longest)
                m[brackets+1] = 0
        return longest

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
    s = temp.replace(", ",",").replace("\"","").replace("[","").replace("]","").rstrip()
    print("s = {0}".format(s))

    sl = Solution()
    time0 = time.time()

    result = sl.longestValidParentheses(s)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
