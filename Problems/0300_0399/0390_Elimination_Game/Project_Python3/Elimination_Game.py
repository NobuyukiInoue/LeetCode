# coding: utf-8

import os
import sys
import time
import collections
from functools import reduce

class Solution:
#   def lastRemaining(self, n: int) -> int:
    def lastRemaining(self, n):
        k, start, end = 1, 1, n
        while True:
            if end == start or end == start + k:
                return end
            if (end - start)%(2*k)==0:
                end = end - k
            start = start + k
            k *= 2
            if end == start or start == end - k:
                return start
            if (end - start)%(2*k) == 0:
                start = start + k
            end -= k
            k *= 2

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()

    n = int(flds)
    print("n = %d" %n)

    time0 = time.time()

    sl = Solution()
    result = sl.lastRemaining(n)

    time1 = time.time()

    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
