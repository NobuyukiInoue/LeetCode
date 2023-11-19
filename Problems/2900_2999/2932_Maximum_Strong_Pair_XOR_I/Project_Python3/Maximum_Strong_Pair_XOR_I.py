import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        # 113ms - 127ms
        n, ans = len(nums), 0
        for i, x in enumerate(nums):
            for j in range(i, n):
                y = nums[j]
                if abs(x - y) <= min(x, y):
                    ans = max(ans, x ^ y)
        return ans

    def maximumStrongPairXor2(self, nums: List[int]) -> int:
        # 164ms - 172ms
        ans = 0
        for x in nums:
            for y in nums:
                if abs(x - y) <= min(x, y):
                    ans = max(ans, x ^ y)
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

    result = sl.maximumStrongPairXor(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
