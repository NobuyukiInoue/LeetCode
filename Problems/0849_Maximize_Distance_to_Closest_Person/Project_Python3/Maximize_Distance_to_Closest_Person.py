# coding: utf-8

import os
import sys
import time

class Solution:
#    def maxDistToClosest(self, seats: List[int]) -> int:
    def maxDistToClosest(self, seats):
        res = i = 0
        for j in range(len(seats)):
            if seats[j]:
                res = max(res, j - i + 1 >> 1) if i else j
                i = j + 1
        return max(res, len(seats) - i)

def str_to_int_array(flds):
    nums = [0]*len(flds)
    for i in range(len(flds)):
        nums[i] = int(flds[i])
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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip().split(",")
    seats = str_to_int_array(flds)
    
    print("seats = %s" %seats)

    time0 = time.time()

    sl = Solution()
    result = sl.maxDistToClosest(seats)
    print("result = %d" %result)

    time1 = time.time()

    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
