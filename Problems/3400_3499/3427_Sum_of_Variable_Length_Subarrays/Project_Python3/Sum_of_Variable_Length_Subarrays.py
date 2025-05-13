import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        # 3ms - 5ms
        ans = 0
        for i, num in enumerate(nums):
            ans += sum(nums[max(0, i - num) : i + 1])
        return ans

    def subarraySum_1liner(self, nums: List[int]) -> int:
        # 6ms - 8ms
        return sum([sum(nums[max(0, i - num) : i + 1]) for i, num in enumerate(nums)])

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

    result = sl.subarraySum(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
