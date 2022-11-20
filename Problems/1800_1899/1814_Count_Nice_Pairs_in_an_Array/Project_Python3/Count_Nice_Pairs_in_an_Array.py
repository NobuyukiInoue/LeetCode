# coding: utf-8

import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        # 1113ms - 2348ms
        dic = collections.defaultdict(int)
        res = 0
        for num in nums:
            temp = num - int(''.join(reversed(list(str(num)))))
            res += dic[temp]
            dic[temp] += 1
        res = res % 1000000007
        return res

    def countNicePairs_1liner(self, nums: List[int]) -> int:
        # 952ms - 1120ms
       return sum(count*(count - 1)//2 for count in collections.Counter(n - int(str(n)[::-1]) for n in nums).values()) % (10**9 + 7)

    def countNicePairs_use_collection(self, nums: List[int]) -> int:
        # 1929ms - 2058ms
        res = 0
        count = collections.Counter()
        for a in nums:
            b = int(str(a)[::-1])
            res += count[a - b]
            count[a - b] += 1
        return res % (10**9 + 7)

    def countNicePairs_bad(self, nums: List[int]) -> int:
        # Time Limit Exceeded.
        def rev(num: int) -> int:
            return int(''.join(reversed(list(str(num)))))
        n = len(nums)
        result = 0
        revs = []
        for i, _ in enumerate(nums):
            revs.append(rev(_))
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + revs[j] == nums[j] + revs[i]:
                    result += 1
        return result

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

    result = sl.countNicePairs(nums)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
