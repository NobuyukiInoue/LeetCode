import collections
import functools
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        # 39ms - 58ms
        ans, cnts = 0, collections.Counter(nums)
        for k, v in cnts.items():
            if v == 2:
                ans ^= k
        return ans

    def duplicateNumbersXOR_2liner(self, nums: List[int]) -> int:
        # 42ms - 57ms
        duplicates = [num for num, cnt in collections.Counter(nums).items() if cnt == 2]
        return functools.reduce(lambda x, y: x ^ y, duplicates, 0)

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

    result = sl.duplicateNumbersXOR(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
