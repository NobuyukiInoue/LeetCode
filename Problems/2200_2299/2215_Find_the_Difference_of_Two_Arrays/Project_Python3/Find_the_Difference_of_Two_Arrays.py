# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # 176ms - 188ms
        return [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]

    def findDifference_useset(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # 180ms - 293ms
        nums1, nums2 = set(nums1), set(nums2)
        ans1, ans2 = [], []
        for _, num in enumerate(nums1):
            if not num in nums2:
                ans1.append(num)
        for _, num in enumerate(nums2):
            if not num in nums1:
                ans2.append(num)
        return [ans1, ans2]

    def findDifference3(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # 980ms - 1530ms
        ans1, ans2 = [], []
        for _, num in enumerate(nums1):
            if not num in nums2 and not num in ans1:
                ans1.append(num)
        for _, num in enumerate(nums2):
            if not num in nums1 and not num in ans2:
                ans2.append(num)
        return [ans1, ans2]

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
    nums1, nums2 = nums[0], nums[1]
    print("nums1 = {0}, nums2 = {1}".format(nums1, nums2))
  
    sl = Solution()
    time0 = time.time()

    result = sl.findDifference(nums1, nums2)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
