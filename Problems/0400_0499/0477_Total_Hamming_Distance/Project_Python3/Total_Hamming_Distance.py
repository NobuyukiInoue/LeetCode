# coding: utf-8

import itertools
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        # 397ms - 460ms
        nums_len = len(nums)
        if nums_len == 0:
            return 0
        current_bit, max_nums = 1, max(nums)
        ret = 0
        while current_bit <= max_nums:
            counter = 0
            for num in nums:
                if num & current_bit:
                    counter += 1
            ret += counter*(nums_len - counter)
            current_bit <<= 1
        return ret

    def totalHammingDistance_comb(self, nums: List[int]) -> int:
        # Time Limit Exceeded.
        def bitCount(x):
            x = x - ((x >> 1) & 0x5555555555555555)
            x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
            x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f
            x = x + (x >> 8)
            x = x + (x >> 16)
            x = x + (x >> 32)
            return x & 0x0000007f
        ans = 0
        for comb in itertools.combinations(nums, 2):
            ans += bitCount(comb[0] ^ comb[1])
        return ans

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

    result = sl.totalHammingDistance(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
