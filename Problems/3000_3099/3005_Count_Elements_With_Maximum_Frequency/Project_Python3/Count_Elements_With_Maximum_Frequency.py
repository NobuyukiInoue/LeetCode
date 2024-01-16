import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # 39ms - 44ms
        cnts = collections.Counter(nums)
        lst = sorted(cnts.items(), key=lambda x:x[1], reverse=True)
        ans, prev_v = 0, lst[0][1]
        for _, v in lst:
            if v == prev_v:
                ans += v
                continue
            break
        return ans

    def maxFrequencyElements2(self, nums: List[int]) -> int:
        # 31ms - 50ms
        cnts = collections.Counter(nums)
        mx = max(cnts.values())
        return sum(filter(lambda x: x == mx, cnts.values()))

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

    result = sl.maxFrequencyElements(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
