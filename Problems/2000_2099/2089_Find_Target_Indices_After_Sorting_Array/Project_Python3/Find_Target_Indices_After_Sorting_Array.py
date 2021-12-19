# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # 44ms
        nums.sort()
        return [i for i, num in enumerate(nums) if num == target]

    def targetIndices2(self, nums: List[int], target: int) -> List[int]:
        # 72ms
        return list(filter(lambda x: (x != -1), [[-1, i][sorted(nums)[i] == target] for i in range(len(nums))]))

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
    target = int(flds[1])
    print("nums = {0}, target = {1:d}".format(nums, target))

    sl = Solution()
    time0 = time.time()

    result = sl.targetIndices(nums, target)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
