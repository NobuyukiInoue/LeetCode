import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 53ms - 54ms
        for j in range(n):
            nums1[m + j] = nums2[j]
        nums1.sort()
    
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
    flds = temp.replace("\"","").replace("[[[","").replace("]]]","").rstrip().split("]],[[")
    flds1 = flds[0].split("],[")
    flds2 = flds[1].split("],[")
    nums1 = [int(val) for val in flds1[0].split(",")]
    m = int(flds1[1])
    nums2 = [int(val) for val in flds2[0].split(",")]
    n = int(flds2[1])

    print("nums1 = {0}, m = {1:d}, nums2 = {2}, n = {3:d}".format(nums1, m, nums2, n))

    sl = Solution()
    time0 = time.time()

    result = sl.merge(nums1, m, nums2, n)

    time1 = time.time()

    print("===result===".format(result))
    print("nums1 = {0}".format(nums1))
    print("nums2 = {0}".format(nums2))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
