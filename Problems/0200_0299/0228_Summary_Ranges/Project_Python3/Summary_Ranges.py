# coding: utf-8

import collections
import os
import sys
import time

class Solution:
#   def summaryRanges(self, nums: List[int]) -> List[str]:
    def summaryRanges(self, nums):
        # 24ms - 40ms
        ranges = []
        for n in nums:
            if not ranges or n > ranges[-1][-1] + 1:
                ranges += [],
            ranges[-1][1:] = n,
        return ['->'.join(map(str, r)) for r in ranges]

    def summaryRanges_work(self, nums):
        # 32ms - 40ms
        res = []
        if len(nums) == 0:
            return res
        n_start, n_end = nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                n_end = nums[i]
            else:
                if n_end > n_start:
                    res.append(str(n_start) + "->" + str(n_end))
                else:
                    res.append(str(nums[i - 1]))
                n_start = nums[i]
                n_end = nums[0]
        if n_end > n_start:
            res.append(str(n_start) + "->" + str(n_end))
        else:
            res.append(str(nums[-1]))
        return res

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()

    nums = [int(n) for n in flds.split(",")]
    print("nums = {0}".format(nums))

    time0 = time.time()

    sl = Solution()
    result = sl.summaryRanges(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
