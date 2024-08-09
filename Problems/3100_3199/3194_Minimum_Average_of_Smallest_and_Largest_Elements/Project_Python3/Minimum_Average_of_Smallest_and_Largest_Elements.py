import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        # 36ms - 43ms
        nums.sort()
        n = len(nums)
        ans = (nums[0] + nums[n - 1])/2
        for i in range(1, n//2 + 1):
            ans = min((nums[i] + nums[n - i - 1])/2, ans)
        return ans

    def minimumAverage2(self, nums: List[int]) -> float:
        # 41ms - 46ms
        nums.sort()
        n = len(nums)
        averages = [(nums[i] + nums[n - i - 1])/2 for i in range(0, n//2 + 1)]
        return min(averages)

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

    result = sl.minimumAverage(nums)

    time1 = time.time()

    print("result = {0:f}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
