# coding: utf-8

import itertools
import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        # 59ms - 68ms
        return collections.Counter(map(sum, itertools.pairwise(nums))).most_common(1)[0][1] >= 2

    def findSubarrays2(self, nums: List[int]) -> bool:
        # 43ms - 86ms
        hash_map = {}
        for i in range(len(nums) - 1):
            t = nums[i] + nums[i + 1]
            if t in hash_map.keys():
                return True
            hash_map[t] = t
        return False

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
    nums = [int(n) for n in flds.split(",")]
    print("nums = {0}".format(nums))

    sl = Solution()

    time0 = time.time()

    result = sl.findSubarrays(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
