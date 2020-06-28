# coding: utf-8

import itertools
import os
import sys
import time
from functools import reduce

class Solution:
#   def getPermutation(self, n: int, k: int) -> str:
    def getPermutation(self, n, k):
        # 28ms
        total, m, out = 1, n - 1, []
        curList = [1 + i for i in range(n)]
        while m > 1:
            total *= m
            m -= 1
        m = n - 1
        k -= 1
        while len(out) != n:
            tmp = k//total 
            out.append(str(curList[tmp]))
            curList = curList[:tmp] + curList[tmp+1:]
            k= k%total
            if m == 0:
                break 
            total = total//m
            m -= 1
        return ''.join(out)

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip().split(",")

    n = int(flds[0])
    k = int(flds[1])
    print("n = {0:d}, k = {1:d}".format(n, k))

    sl = Solution()
    time0 = time.time()

    result = sl.getPermutation(n, k)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
