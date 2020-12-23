# coding: utf-8

import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # 52ms
        left, right = 0, len(nums) - 1
        while left <=  right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[left] <= nums[mid]:
                if nums[left] == nums[mid] and mid != left:
                    left += 1
                    continue
                if nums[left] <= target< nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[left] > nums[mid]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else: right = mid - 1
        return False

    def search2(self, nums: List[int], target: int) -> bool:
        # 92ms
        return [] != [num for num in nums if num == target]

    def search3(self, nums: List[int], target: int) -> bool:
        # 100ms
        if target in nums:
            return True
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
    flds = temp.replace("[[","").replace("]]","").replace("\"","").replace(" ","").rstrip().split("],[")

    nums = [int(n) for n in flds[0].split(",")]
    target = int(flds[1])
    print("nums = {0}, target = {1:d}".format(nums, target))

    sl = Solution()

    time0 = time.time()

    result = sl.search(nums, target)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
