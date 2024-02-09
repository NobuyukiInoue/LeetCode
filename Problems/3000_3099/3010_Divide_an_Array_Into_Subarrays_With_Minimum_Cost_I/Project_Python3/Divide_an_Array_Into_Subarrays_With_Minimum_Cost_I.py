import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # 88ms
        n, ans = len(nums), sys.maxsize
        for i in range (1, n - 1):
            for j in range(1, n - i):
                ans = min(ans, nums[0] + nums[i] + nums[i + j])
        return ans

    def minimumCost2(self, nums: List[int]) -> int:
        # 50ms - 51ms
        n = len(nums)
        nums[1:n] = sorted(nums[1:n])
        return nums[0] + nums[1] + nums[2]

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

    result = sl.minimumCost(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
