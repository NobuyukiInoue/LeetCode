import math
import itertools
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def minimumSumSubarray1(self, nums: List[int], l: int, r: int) -> int:
        # 18ms - 19ms
        n = len(nums)
        min_sum = float('inf')
        for length in range(l, r + 1):
            if length > n:
                continue
            window_sum = sum(nums[:length])
            if window_sum > 0:
                min_sum = min(min_sum, window_sum)
            for i in range(length, n):
                window_sum += nums[i] - nums[i - length]
                if window_sum > 0:
                    min_sum = min(min_sum, window_sum)
        return min_sum if min_sum  < float('inf') else -1

    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        # 85ms - 90ms
        n = len(nums)
        length, min_sum = l, sys.maxsize
        for length in range(l, r + 1):
            for i in range(n):
                if i + length <= n:
                    v_sum = sum(nums[i:i + length])
                    if v_sum > 0:
                        min_sum = min(min_sum, v_sum)
        if min_sum == sys.maxsize:
            return -1
        return min_sum

    def minimumSumSubarray3(self, nums: List[int], l: int, r: int) -> int:
        # 51ms - 54ms
        n, mn = len(nums), math.inf
        acc = list(itertools.accumulate(nums, initial = 0))
        for left in range(n):
            for rght in range(left + 1, n + 1):
                sm, length = acc[rght] - acc[left], rght - left
                if l <= length <= r and 0 < sm < mn:
                    mn = sm 
        return -1 if mn == math.inf else mn

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
    
    nums, l, r = [int(num) for num in flds[0].split(",")], int(flds[1]), int(flds[2])
    print("nums = {0}, l = {1:d}, r = {2:d}".format(nums, l, r))

    sl = Solution()
    time0 = time.time()

    result = sl.minimumSumSubarray(nums, l, r)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
