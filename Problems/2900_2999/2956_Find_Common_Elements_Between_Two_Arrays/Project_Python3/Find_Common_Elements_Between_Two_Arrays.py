import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def findIntersectionValues_1liner(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 161ms - 165ms
         return [sum(num in nums2 for num in nums1), sum(num in nums1 for num in nums2)]

    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 152ms - 168ms
        res1, res2 = 0, 0
        for num in nums1:
            if num in nums2:
                res1 += 1
        for num in nums2:
            if num in nums1:
                res2 += 1
        return [res1, res2]

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
    print("nums1 = {0}, nums2 =  {1}".format(nums1, nums2))

    sl = Solution()
    time0 = time.time()

    result = sl.findIntersectionValues(nums1, nums2)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
