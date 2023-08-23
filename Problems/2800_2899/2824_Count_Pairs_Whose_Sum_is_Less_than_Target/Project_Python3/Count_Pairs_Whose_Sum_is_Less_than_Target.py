import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # 48ms - 54ms
        ans, n = 0, len(nums)
        nums.sort()
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] >= target:
                    break
                ans += 1
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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")

    nums = [int(n) for n in flds[0].split(",")]
    target = int(flds[1])
    print("nums = {0}, target = {1:d}".format(nums, target))

    sl = Solution()
    time0 = time.time()

    result = sl.countPairs(nums, target)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
