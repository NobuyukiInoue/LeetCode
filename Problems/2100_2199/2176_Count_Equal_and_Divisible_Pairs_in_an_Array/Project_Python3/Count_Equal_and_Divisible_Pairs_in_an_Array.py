# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # 72ms
        counter = {}
        for i, _ in enumerate(nums):
            if nums[i] in counter:
                counter[nums[i]].append(i)
            else:
                counter[nums[i]] = [i]
        ans = 0
        for _, val in counter.items():
            length = len(val)
            for i in range(length - 1):
                for j in range(i + 1, length):
                    if val[i] * val[j] % k == 0:
                        ans += 1
        return ans

    def countPairs_twoloop(self, nums: List[int], k: int) -> int:
        # 114ms
        ans, len_nums = 0, len(nums)
        for i, _ in enumerate(nums):
            for j in range(i + 1, len_nums):
                if nums[i] != nums[j]:
                    continue
                if i*j % k == 0:
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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    nums = [int(n) for n in flds[0].split(",")]
    k = int(flds[1])
    print("nums = {0}, k = {1:d}".format(nums, k))

    sl = Solution()
    time0 = time.time()

    result = sl.countPairs(nums, k)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
