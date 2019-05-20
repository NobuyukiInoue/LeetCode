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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()

    seats = [int(n) for n in flds.split(",")]
    print("seats = %s" %seats)

    time0 = time.time()

    sl = Solution()
    result = sl.maxDistToClosest(seats)

    time1 = time.time()

    print("result = %d" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
