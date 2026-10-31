import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        # 1ms
        cnt, total, ans = len(nums), sum(nums), 0
        for num in nums:
            total -= num
            cnt -= 1
            ans += (num*cnt > total)
        return ans

    def dominantIndices2(self, nums: List[int]) -> int:
        # 3ms
        n, total = len(nums), sum(nums)
        cnt, curr = 0, 0
        for i in range(n - 1):
            curr += nums[i]
            if n - i - 1 > 0 and (total - curr) // (n - i - 1) < nums[i]:
                cnt += 1
        return cnt

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

    result = sl.dominantIndices(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
