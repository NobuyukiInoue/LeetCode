import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        # 84ms - 95ms
        n = len(nums)
        pos1, pos2 = nums.index(1), nums.index(n)
        return pos1 + n - pos1 - pos2 - (pos1 > pos2)

    def semiOrderedPermutation2(self, nums: List[int]) -> int:
        # 88ms
        n = len(nums)
        for i, num in enumerate(nums):
            if num == 1:
                pos1 = i
            elif num == n:
                pos2 = i
        return pos1 + n - pos2 - 1 - (pos1 > pos2)

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

    result = sl.semiOrderedPermutation(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
