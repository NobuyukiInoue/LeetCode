# coding: utf-8

import bisect
import itertools
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # 109ms - 144ms
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return ([bisect.bisect_right(nums, q) for q in queries])

    def answerQueries2(self, nums: List[int], queries: List[int]) -> List[int]:
        # 191ms - 264ms
        nums = list(itertools.accumulate(sorted(nums)))
        return [bisect.bisect_right(nums, q) for q in queries]

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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    nums = [int(n) for n in flds[0].split(",")]
    queries = [int(n) for n in flds[1].split(",")]
    print("nums = {0}, k = {1}".format(nums, queries))

    sl = Solution()
    time0 = time.time()

    result = sl.answerQueries(nums, queries)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
