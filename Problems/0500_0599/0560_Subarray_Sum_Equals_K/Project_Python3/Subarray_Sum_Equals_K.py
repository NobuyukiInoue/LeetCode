# coding: utf-8

import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 248ms
        preSums = {0: 1}
        s = 0
        res = 0
        for num in nums:
            s += num
            res += preSums.get(s - k, 0)
            preSums[s] = preSums.get(s, 0) + 1
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
    flds = temp.replace("[[","").replace("]]","").replace("\"","").replace(" ","").rstrip().split("],[")
    nums = [int(n) for n in flds[0].split(",")]
    k = int(flds[1])
    print("nums = {0}, k = {1:d}".format(nums, k))

    sl = Solution()

    time0 = time.time()

    result = sl.subarraySum(nums, k)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
