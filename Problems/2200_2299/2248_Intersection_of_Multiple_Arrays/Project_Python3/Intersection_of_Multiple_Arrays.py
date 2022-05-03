# coding: utf-8

import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def intersection_oneliner(self, nums: List[List[int]]) -> List[int]:
        # 81ms - 102ms
        return sorted([k for k, v in collections.Counter([x for l in nums for x in l]).items() if v == len(nums)])

    def intersection(self, nums: List[List[int]]) -> List[int]:
        # 66ms - 101ms
        arr = [x for num in nums for x in num]
        cnts = collections.Counter(arr)
        ans = [k for k, v in cnts.items() if v == len(nums)]
        return sorted(ans)

    """
    def intersection(self, nums):
        # 91ms - 99ms
        return sorted(reduce(lambda a,b: a & b, map(set, nums)))

    def intersection(self, nums):
        # 77ms - 90ms
        return sorted(reduce(operator.__and__, map(set, nums)))

    def intersection(self, nums):
        # 77ms - 81ms
        return sorted(reduce(set.intersection, map(set, nums)))

    def intersection(self, nums):
        # 77ms - 80ms
        return sorted(set.intersection(*map(set, nums)))
    """

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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip()

    nums = [[int(col) for col in data.split(",")] for data in flds.split("],[")]
    print("nums = {0}".format(nums))
  
    sl = Solution()
    time0 = time.time()

    result = sl.intersection(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
