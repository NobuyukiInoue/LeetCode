import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        # 139ms
        n = len(nums)
        nums.sort()
        score = nums[-1] - nums[0]
        res = score
        for i in range(0, n - 1):
            v_max = max(nums[i] + k , nums[-1] - k)
            v_min = min(nums[i + 1] - k , nums[0] + k)
            score = v_max - v_min
            res = min(res, score)
        return res

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
    k = int(flds[1])
    print("nums = {0}, k = {1:d}".format(nums, k))

    sl = Solution()
    time0 = time.time()

    result = sl.smallestRangeII(nums, k)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
