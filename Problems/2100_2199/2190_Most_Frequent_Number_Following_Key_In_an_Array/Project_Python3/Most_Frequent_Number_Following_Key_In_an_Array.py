# coding: utf-8

import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        # 80ms
        cnts = {}
        target, max_cnts = 0, 0
        for i in range(len(nums) - 1):
            if nums[i] == key:
                if nums[i + 1] not in cnts:
                    cnts[nums[i + 1]] = 1
                else:
                    cnts[nums[i + 1]] += 1
                if max_cnts < cnts[nums[i + 1]]:
                    target, max_cnts = nums[i + 1], cnts[nums[i + 1]]
        return target

    def mostFrequent2(self, nums: List[int], key: int) -> int:
        # 84ms
        cnts = collections.Counter()
        for i, num in enumerate(nums):
            if num == key and i + 1 < len(nums):
                cnts[nums[i + 1]] += 1
        return cnts.most_common(1)[0][0]

    def mostFrequent3(self, nums: List[int], key: int) -> int:
        # 84ms
        cnts = collections.Counter()
        target, max_cnts = 0, 0
        for i in range(len(nums) - 1):
            if nums[i] == key:
                cnts[nums[i + 1]] += 1
                if max_cnts < cnts[nums[i + 1]]:
                    target, max_cnts = nums[i + 1], cnts[nums[i + 1]]
        return target

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
    key = int(flds[1])
    print("nums = {0}, key = {1:d}".format(nums, key))

    sl = Solution()
    time0 = time.time()

    result = sl.mostFrequent(nums, key)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
