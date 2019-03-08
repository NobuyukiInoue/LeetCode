# coding: utf-8

import collections
import os
import sys
import time

class Solution:
#    def findLHS(self, nums: List[int]) -> int:
    def findLHS(self, nums):
        count = collections.Counter(nums)
        return max([count[x] + count[x+1] for x in count if count[x+1]] or [0])

def str_to_int_array(flds):
    if len(flds) <= 0:
        return None
    temp = flds.split(",")
    nums = [0]*len(temp)
    for i in range(len(temp)):
        nums[i] = int(temp[i])
    return nums

def main():
    argv = sys.argv
    argc = len(argv)

    if (argc < 2):
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
    flds = temp.replace(" ","").replace("[","").replace("]","").rstrip()
    nums = str_to_int_array(flds)

    time0 = time.time()

    sl = Solution()
    result = sl.findLHS(nums)

    time1 = time.time()

    print("result = %d" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
