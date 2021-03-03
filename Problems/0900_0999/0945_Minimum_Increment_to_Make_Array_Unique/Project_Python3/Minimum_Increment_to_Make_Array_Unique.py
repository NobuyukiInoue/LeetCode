# coding: utf-8

import collections
import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        # 280ms
        A.sort()
        last = -sys.maxsize
        res = 0
        for a in A:
            if a <= last:
                last += 1
                res += last - a
            else: 
                last = a
        return res

    def minIncrementForUnique2(self, A):
        # 316ms
        res = need = 0
        for i in sorted(A):
            res += max(need - i, 0)
            need = max(need + 1, i + 1)
        return res

    def minIncrementForUnique2(self, A: List[int]) -> int:
        # Time Limit Exceeded.
        dic = collections.Counter(A)
        print(dic)
        indexs = sorted(dic)
        print(indexs)
        res = 0
        for i, index in enumerate(indexs):
            print("i = {0:d}, dic[{1:d}] = {2:d}".format(i, index, dic[index]))
            while dic[index] > 1:
                j = index
                while dic[j] > 0:
                    j += 1
                    res += 1
                dic[j] = 1
                print("dic[{0:d}] = {1:d}".format(j, dic[j]))
                dic[index] -= 1
        print(dic)
        return res

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
    flds = temp.replace("[","").replace("]","").replace(", ",",").rstrip()

    A = [int(n) for n in flds.split(",")]
    print("A = {0}".format(A))

    sl = Solution()

    time0 = time.time()

    result = sl.minIncrementForUnique(A)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
