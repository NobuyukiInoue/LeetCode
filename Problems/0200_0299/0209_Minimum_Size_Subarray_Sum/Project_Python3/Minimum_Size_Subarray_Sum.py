# coding: utf-8

import os
import sys
import time

class Solution:
#   def minSubArrayLen(self, s: int, nums: List[int]) -> int:
    def minSubArrayLen(self, s, nums):
        # 72ms
        i, res = 0, len(nums) + 1
        for j in range(len(nums)):
            s -= nums[j]
            while s <= 0:
                res = min(res, j - i + 1)
                s += nums[i]
                i += 1
        return res % (len(nums) + 1)

    def minSubArrayLen_bad(self, s, nums):
        if len(nums) <= 0:
            return 0

        nums.reverse()

        def helper(total, index, length):
            for i in range(index, len(nums)):
                if nums[i] > total:
                    continue
                if total <= nums[i]:
                    return length + 1
                else:
                    return helper(total - nums[i], 1, length + 1)

        return helper(s, 0, 0)


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
    flds = temp.replace("[[","").replace("]]","").replace("\"","").replace(" ","").rstrip().split("],[")

    s = int(flds[0])
    if len(flds[1]) > 0:
        nums = [int(n) for n in flds[1].split(",")]
    else:
        nums = []
    print("s = {0}, nums = {1}".format(s, nums))

    time0 = time.time()

    sl = Solution()
    result = sl.minSubArrayLen(s, nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
