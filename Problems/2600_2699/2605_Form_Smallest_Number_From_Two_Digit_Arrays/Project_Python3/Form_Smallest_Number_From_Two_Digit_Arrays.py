# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        # 35ms - 39ms
        nums1.sort()
        nums2.sort()
        for _, n in enumerate(nums1):
            if n in nums2:
                return n
        return 10*nums1[0] + nums2[0] if nums1[0] < nums2[0] else 10*nums2[0] + nums1[0]

    def minNumber2(self, nums1: List[int], nums2: List[int]) -> int:
        # 35ms - 44ms
        inter = set(nums1) & set(nums2)
        if inter:
            return min(inter)
        d1, d2 = min(nums1), min(nums2)
        return 10*d1 + d2 if d1 < d2 else 10*d2 + d1

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

    nums1 = [int(col) for col in flds[0].split(",")]
    nums2 = [int(col) for col in flds[1].split(",")]
    print("nums1 = {0}, nums2 = {1}".format(nums1, nums2))

    sl = Solution()
    time0 = time.time()

    result = sl.minNumber(nums1, nums2)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
