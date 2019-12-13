# coding: utf-8

import os
import sys
import time

class Solution:
#   def jump(self, nums: List[int]) -> int:
    def jump(self, nums):
        # 104ms
        n, start, end, step = len(nums), 0, 0, 0
        while end < n - 1:
            step += 1
            maxend = end + 1
            for i in range(start, end + 1):
                if i + nums[i] >= n - 1:
                    return step
                maxend = max(maxend, i + nums[i])
            start, end = end + 1, maxend
        return step

    def jump2(self, nums):
        # Time Limit Exceeded
        track = [0]*len(nums)
        for i in range(1, len(nums)):
            min = sys.maxsize
            for j in range(i):
                if track[j] < min and nums[j] + j >= i:
                    min = track[j]
            track[i] = min + 1

        return track[len(nums) - 1]

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
    result = sl.jump(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
