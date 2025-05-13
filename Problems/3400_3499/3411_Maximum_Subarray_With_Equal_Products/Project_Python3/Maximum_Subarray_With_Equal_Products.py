import math
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        # 3ms - 4ms
        n, ans = len(nums), 2
        for i in range(n - 1):
            v_gcd = v_lcm = nums[i]
            for j in range(i + 1, n):
                v_gcd = math.gcd(v_gcd, nums[j])
                if v_gcd != 1 or math.gcd(v_lcm, nums[j]) != 1:
                    ans = max(ans, j - i)
                    break
                v_lcm *= nums[j]
            else:
                ans = max(ans, j - i + 1)
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

    result = sl.maxLength(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
