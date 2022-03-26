# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        # 336ms - 626ms
        sums = []
        for i, _ in enumerate(nums):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                sums.append(current_sum)
        sums.sort()
        return sum(sums[left - 1:right]) % (pow(10, 9) + 7)

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
    n, left, right = int(flds[1]), int(flds[2]), int(flds[3])

    print("nums = {0}, n = {1:d}, left = {2:d}, right = {3:d}".format(nums, n, left, right))

    sl = Solution()
    time0 = time.time()

    result = sl.rangeSum(nums, n, left, right)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
