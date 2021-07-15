# coding: utf-8

import collections
import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def countTriples(self, n: int) -> int:
        # 284ms
        square = {i:i**2 for i in range(n + 1)}
        dict_ = collections.defaultdict(int)
        for i in range(1,n + 1):
            for j in range(i+1, n+1):
                dict_[-square[i] - square[j]] += 2
        return sum(dict_[-square[i]] for i in range(1, n + 1))

    def countTriples2(self, n: int) -> int:
        # 396ms
        ans = 0
        nums = [i for i in range(n + 1)]
        for i in range(n, 0, -1):
            l, r = 0, i - 1
            while l < r:
                if nums[l]*nums[l]+nums[r]*nums[r] == nums[i]*nums[i]:
                    ans += 2
                    l += 1
                    r -= 1
                elif nums[l]*nums[l]+nums[r]*nums[r] < nums[i]*nums[i]:
                    l += 1
                else:
                    r -= 1
        return ans

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

    n = int(flds)
    print("n = {0:d}".format(n))

    sl = Solution()

    time0 = time.time()

    result = sl.countTriples(n)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
