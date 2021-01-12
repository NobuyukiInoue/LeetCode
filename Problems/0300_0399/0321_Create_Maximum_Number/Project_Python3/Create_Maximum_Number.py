# coding: utf-8

import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        N1 = len(nums1)
        N2 = len(nums2)

        def get_candidate(nums, start, max_skip):
            j = start
            v = -1
            for i in range(start, min(len(nums), start + max_skip + 1)):
                if v < nums[i]:
                    j = i
                    v = nums[j]
                    if nums[j] == 9:break
            return j, v

        next_candidates = {(0, 0)}
        ret = [0]*k
        for remain in range(k, 0, -1):
            candidates = next_candidates
            next_candidates = set()
            value_max = -1
            for (i1, i2) in candidates:
                if i1 >= N1 and i2 >= N2: continue
                r1 = N1 - i1
                r2 = N2 - i2
                max_skip = r1 + r2 - remain

                j1, v1 = get_candidate(nums1, i1, max_skip)
                j2, v2 = get_candidate(nums2, i2, max_skip)

                if v1 > value_max:
                    next_candidates = {(j1 + 1, i2)}
                    value_max = v1
                elif v1 == value_max:
                    next_candidates.add((j1 + 1, i2))
                
                if v2 > value_max:
                    next_candidates = {(i1, j2 + 1)}
                    value_max = v2
                elif v2 == value_max:
                    next_candidates.add((i1, j2 + 1))
            ret[-remain] = value_max
        return ret

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

    nums1 = [int(n) for n in flds[0].split(",")]
    nums2 = [int(n) for n in flds[1].split(",")]
    k = int(flds[2])
    print("nums1 = {0}, nums2 = {1}, k = {2:d}".format(nums1, nums2, k))

    sl = Solution()

    time0 = time.time()

    result = sl.maxNumber(nums1, nums2, k)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
