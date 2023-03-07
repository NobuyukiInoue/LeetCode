# coding: utf-8

import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # 1095ms - 1108ms
        dict_map, max_val = {}, -1
        for i, num in enumerate(nums):
            digits_sum = 0
            while num > 0:
                digits_sum += num % 10
                num //= 10
            if digits_sum in dict_map:
                new_max_val = nums[i] + dict_map[digits_sum]
                max_val = max(max_val, new_max_val)
                dict_map[digits_sum] = max(nums[i], dict_map[digits_sum])
            else:
                dict_map[digits_sum] = nums[i]
        return max_val

    def maximumSum2(self, nums: List[int]) -> int:
        # 1300ms - 1370ms
        dict_map, max_val = collections.defaultdict(lambda: -sys.maxsize), -1         
        for v in nums:
            d = sum(map(int, list(str(v)))) 
            max_val = max(max_val, v + dict_map[d])
            dict_map[d] = max(v, dict_map[d])
        return max_val

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
    flds = temp.replace("[","").replace("]","").replace(", ",",").rstrip()
    nums = [int(n) for n in flds.split(",")]
    print("nums = {0}".format(nums))

    sl = Solution()

    time0 = time.time()

    result = sl.maximumSum(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
