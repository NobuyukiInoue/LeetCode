import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # 442ms - 485ms
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                return nums1[i]
        return -1

    def getCommon2(self, nums1: List[int], nums2: List[int]) -> int:
        # 461ms - 495ms
        i, len2 = 0, len(nums2)
        for n1 in nums1:
            while i < len2 and nums2[i] < n1:
                i += 1
            if i < len2 and n1 == nums2[i]:
                return n1
        return -1    

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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")

    nums1 = [int(n) for n in flds[0].split(",")]
    nums2 = [int(n) for n in flds[1].split(",")]
    print("nums1 = {0}".format(nums1))
    print("nums2 = {0}".format(nums2))

    sl = Solution()
    time0 = time.time()

    result = sl.getCommon(nums1, nums2)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
