# coding: utf-8

import itertools
import os
import sys
import time

from functools import reduce


class Solution:
#   def permute(self, nums: List[int]) -> List[List[int]]:
    def permute1(self, nums):
        # 60ms
        return [[n] + p
                for i, n in enumerate(nums)
                for p in self.permute(nums[:i] + nums[i+1:])] or [[]]

    def permute2(self, nums):
        # 32ms
        return nums and [p[:i] + [nums[0]] + p[i:]
                        for p in self.permute(nums[1:])
                        for i in range(len(nums))] or [[]]

    def permute3(self, nums):
        # 32ms
        return reduce(lambda P, n: [p[:i] + [n] + p[i:]
                    for p in P for i in range(len(p)+1)],
                    nums, [[]])

    def permute4(self, nums):
        # 36ms
        return map(list, itertools.permutations(nums))

    def permute5(self, nums):
        # 32ms
        return list(itertools.permutations(nums))

    def permute(self, nums):
        # 32ms
        return nums and [p[:i] + [nums[0]] + p[i:]
                        for p in self.permute(nums[1:])
                        for i in range(len(nums))] or [[]]


def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
        print("Usage: python %s <testdata.txt>" %(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("%s not found..." %argv[1])
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        temp = temp.strip()
        if temp == "":
            continue
        print("args = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip().split(",")
    nums = [int(n) for n in flds]

    time0 = time.time()

    sl = Solution()
    result = sl.permute(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
