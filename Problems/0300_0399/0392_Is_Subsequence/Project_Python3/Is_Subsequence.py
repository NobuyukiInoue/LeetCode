import math
import os
import collections
import sys
import time
from functools import reduce

class Solution:
#   def isSubsequence(self, s: str, t: str) -> bool:
    def isSubsequence2(self, s, t):
        # 296ms
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False 
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        if i == len(s):
            return True
        else:
            return False

    def isSubsequence(self, s, t):
        # 40ms
        ind = -1
        for i in s:
            try: ind = t.index(i,ind+1)
            except: return False
        return True

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
    flds = temp.replace(", ",",").replace("\"","").replace("[","").replace("]","").rstrip().split(",")
    s = flds[0]
    t = flds[1]
    print("s = {0}, t = {1}".format(s, t))

    sl = Solution()
    time0 = time.time()
    result = sl.isSubsequence(s, t)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
