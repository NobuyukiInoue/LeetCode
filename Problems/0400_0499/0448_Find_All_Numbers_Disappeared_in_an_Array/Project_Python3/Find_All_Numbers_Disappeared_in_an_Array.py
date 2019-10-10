# coding: utf-8

import os
import sys
import time

class Solution:
#    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    def findDisappearedNumbers(self, nums):
        l = len(nums)
        nums = set(nums)
        return [i for i in range(1, l + 1) if i not in nums]

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


def loop_main(temp):
    flds = temp.replace("[","").replace("]","").rstrip().split(",")

    nums = [0]*len(flds)
    for i in range(len(flds)):
        nums[i] = int(flds[i])

    time0 = time.time()

    sl = Solution()
    result = sl.findDisappearedNumbers(nums)
    print("result = %s" %result)

    time1 = time.time()

    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
