import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        # 43ms - 51ms
        return min(nums2) - min(nums1)

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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    
    nums1 = [int(num) for num in flds[0].split(",")]
    nums2 = [int(num) for num in flds[1].split(",")]
    print("nums1 = {0}, nums2 = {1}".format(nums1, nums2))

    sl = Solution()
    time0 = time.time()

    result = sl.addedInteger(nums1, nums2)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
