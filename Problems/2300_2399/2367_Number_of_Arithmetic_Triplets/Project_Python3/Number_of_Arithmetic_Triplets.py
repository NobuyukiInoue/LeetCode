# coding: utf-8

import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        # 26ms - 66ms
        occ = collections.Counter(nums)
        count = 0
        for num in nums:
            if (num + diff) in occ and (2*(num + diff) - num) in occ:
                count += 1
        return count

    def arithmeticTriplets_3loop(self, nums: List[int], diff: int) -> int:
        # 112ms - 180ms
        ans = 0
        for i in range(0, len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                if abs(nums[i] - nums[j]) == diff:
                    for k in range(j + 1, len(nums)):
                        if abs(nums[j] - nums[k]) == diff:
                            ans += 1
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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    nums = [int(n) for n in flds[0].split(",")]
    diff = int(flds[1])

    print("nums = {0}, diff = {1:d}".format(nums, diff))

    sl = Solution()
    time0 = time.time()

    result = sl.arithmeticTriplets(nums, diff)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
