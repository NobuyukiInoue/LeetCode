# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        # 65ms - 74ms
        return [int(ch) for num in nums for ch in str(num)]

    def separateDigits2(self, nums: List[int]) -> List[int]:
        # 72ms - 77ms
        ans = []
        for num in nums:
            if num >= 10:
                temp = []
                while num > 0:
                    temp.append(num % 10)
                    num //= 10
                for i in range(len(temp) - 1, -1, -1):
                    ans.append(temp[i])
            else:
                ans.append(num)
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

    result = sl.separateDigits(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
