# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        # 66ms - 67ms
        res = []
        i, j = 0, 0
        while i < len(nums1) or j < len(nums2):
            if i == len(nums1):
                res.append(nums2[j])
                j += 1
            elif j == len(nums2):
                res.append(nums1[i])
                i += 1
            else:
                if nums1[i][0] == nums2[j][0]:
                    res.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                    i += 1
                    j += 1
                elif nums1[i][0] < nums2[j][0]:
                    res.append(nums1[i])
                    i += 1
                else:
                    res.append(nums2[j])
                    j += 1
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
    flds = temp.replace(" ","").replace("\"","").replace("[[[","").replace("]]]","").rstrip().split("]],[[")

    nums1 = [[int(col) for col in data.split(",")] for data in flds[0].split("],[")]
    nums2 = [[int(col) for col in data.split(",")] for data in flds[1].split("],[")]
    print("nums1 = {0}, nums2 = {1}".format(nums1, nums2))

    sl = Solution()
    time0 = time.time()

    result = sl.mergeArrays(nums1, nums2)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
