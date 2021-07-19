# coding: utf-8

import collections
import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # 712ms
        count = collections.Counter(a + b for a in nums1 for b in nums2)
        ans = 0
        for c in nums3:
            for d in nums4:
                if -(c + d) in count:
                    ans += count[-(c + d)]
        return ans

    def fourSumCount2(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # 716ms
        res1 = [a + b for a in nums1 for b in nums2]
        count = collections.Counter([c + d for c in nums3 for d in nums4])
        return sum(count.get(-1*r1, 0) for r1 in res1)

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

    nums = [[int(n) for n in fld.split(",")] for fld in flds]
    nums1, nums2, nums3, nums4 = nums[0], nums[1], nums[2], nums[3]
    print("nums1 = {0}, nums2 = {1}, nums3 = {2}, nums4 = {3}".format(nums1, nums2, nums3, nums4))

    sl = Solution()

    time0 = time.time()

    result = sl.fourSumCount(nums1, nums2, nums3, nums4)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
