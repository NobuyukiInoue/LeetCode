# coding: utf-8

import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # 1188ms
        left = 0
        nums.sort()
        for right in range(len(nums)):
            k += nums[right]
            if k < nums[right]*(right - left + 1):
                k -= nums[left]
                left += 1
        return right - left + 1

    def maxFrequency2(self, nums: List[int], k: int) -> int:
        # 1868ms
        nums.sort()
        left, right = 0, 0
        totalSum, res = 0, 1
        while right < len(nums):
            totalSum += nums[right]
            while not (totalSum + k >= ((right - left + 1)*nums[right])):
                totalSum -= nums[left]
                left += 1
            res = max(res, (right - left + 1))
            right += 1
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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    nums = [int(n) for n in flds[0].split(",")]
    k = int(flds[1])
    print("nums = {0}, k = {1:d}".format(nums, k))

    sl = Solution()
    time0 = time.time()

    result = sl.maxFrequency(nums, k)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
