# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        # 1120ms
        i, res = 0, 0
        for j, b in enumerate(nums2):
            while i < len(nums1) and nums1[i] > b:
                i += 1
            if i == len(nums1):
                break
            res = max(res, j - i)
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

    nums1 = [int(_) for _ in flds[0].split(",")]
    nums2 = [int(_) for _ in flds[1].split(",")]
    print("nums1 = {0}".format(nums1))
    print("nums2 = {0}".format(nums2))

    sl = Solution()
    time0 = time.time()

    result = sl.maxDistance(nums1, nums2)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
