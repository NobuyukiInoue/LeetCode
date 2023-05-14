import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def distinctDifferenceArray_1liner(self, nums: List[int]) -> List[int]:
        # 123ms - 128ms
        return [(len(set(nums[: i + 1])) - len(set(nums[i + 1 : ]))) for i, _ in enumerate(nums)]

    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        # 125ms - 135ms
        ans = []
        suff = collections.Counter(nums)
        pref = collections.defaultdict(int)
        for _, num in enumerate(nums):
            pref[num] += 1
            suff[num] -= 1
            if suff[num] == 0:
                suff.pop(num)
            ans.append(len(pref) - len(suff))
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

    result = sl.distinctDifferenceArray(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
