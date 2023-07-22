import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        # 70ms - 75ms
        n = len(nums)
        special = [nums[i - 1] for i in range(1, n + 1) if n%(i) == 0]
        return sum([i**2 for i in special])

    def sumOfSquares_1liner(self, nums: List[int]) -> int:
        # 75ms - 80ms
        return sum([nums[i]*nums[i] for i in range(len(nums)) if len(nums)%(i + 1) == 0])
    
    def sumOfSquares2(self, nums: List[int]) -> int:
        # 76ms - 82ms
        ans, n = 0, len(nums)
        for i, num in enumerate(nums):
            if n%(i + 1) == 0:
                ans += num*num
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

    result = sl.sumOfSquares(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
