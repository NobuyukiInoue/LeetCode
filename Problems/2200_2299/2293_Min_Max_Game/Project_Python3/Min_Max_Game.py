# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        # 56ms
        return nums[0] if len(nums) == 1 else self.minMaxGame([(max if i%2 else min)(nums[2*i],nums[2*i+1]) for i in range(len(nums)//2)])

    def minMaxGame_normal(self, nums: List[int]) -> int:
        # 56ms - 140ms
        while len(nums) > 1:
            arr = []
            for i in range(0, len(nums)//2):
                if i % 2 == 0:
                    arr.append(min(nums[2*i : 2*i + 2]))
                else:
                    arr.append(max(nums[2*i : 2*i + 2]))
            nums = arr
        return nums[0]

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

    result = sl.minMaxGame(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
