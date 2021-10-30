# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # 33ms
    #   start, end = max(nums), sum(nums)
        start, end = 0, 0
        for num in nums:
            start = max(start, num)
            end += num
        while start < end:
            mid = start + (end - start)//2
            total, pieces = 0, 1
            for num in nums:
                if total + num > mid:
                    total = num
                    pieces += 1
                else:
                    total += num
            if pieces > m:
                start = mid + 1
            else:
                end = mid
        return end

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

    nums = [int(n) for n in flds[0].split(",")]
    m = int(flds[1])
    print("nums = {0}, k = {1:d}".format(nums, m))

    sl = Solution()
    time0 = time.time()

    result = sl.splitArray(nums, m)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
