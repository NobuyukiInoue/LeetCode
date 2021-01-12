# coding: utf-8

import bisect
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        # 148ms
        count, s = 0, 0
        sorted_sums = [0]
        for x in nums:
            s += x
            l = bisect.bisect_left(sorted_sums, s - upper)
            r = bisect.bisect_right(sorted_sums, s - lower)
            count += r - l
            bisect.insort(sorted_sums, s)
        return count

    def countRangeSum_bad(self, nums: List[int], lower: int, upper: int) -> int:
        # Time Limit Exceeded.
        res = 0
        numsLen = len(nums)
        for i in range(numsLen):
            currentSum = nums[i]
            if lower <= currentSum <= upper:
                res += 1
            for j in range(i + 1, numsLen):
                currentSum += nums[j]
                if lower <= currentSum <= upper:
                    res += 1
        return res

    def countRangeSum_work(self, nums: List[int], lower: int, upper: int) -> int:
        # Time Limit Exceeded.
        res = []
        numsLen = len(nums)
        for i in range(numsLen):
            currentSum = nums[i]
            if lower <= currentSum <= upper:
              # print("[{0:d}:{0:d}]".format(i))
                res.append(currentSum)
            for j in range(i + 1, numsLen):
                currentSum += nums[j]
                if lower <= currentSum <= upper:
                  # print("[{0:d}:{1:d}]".format(i, j))
                    res.append(currentSum)
        return len(res)

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
    lower, upper = int(flds[1]), int(flds[2])
    print("nums = {0}, lower = {1}, upper = {2}".format(nums, lower, upper))

    sl = Solution()
    time0 = time.time()

    result = sl.countRangeSum(nums, lower, upper)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
