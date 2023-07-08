import math
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        # 387ms - 388ms
        ans = 0
        for i, num in enumerate(nums):
            m = num%10
            for j in range(i):
                n = nums[j]
                while n >= 10:
                    n //= 10
                if math.gcd(m, n) == 1:
                    ans += 1
        return ans

    def countBeautifulPairs_1liner(self, nums: List[int]) -> int:
        return sum(sum(math.gcd(int(str(nums[i])[0]),int(str(nums[j])[-1]))==1 for j in range(i + 1, len(nums))) for i in range(len(nums)))
    
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

    result = sl.countBeautifulPairs(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
