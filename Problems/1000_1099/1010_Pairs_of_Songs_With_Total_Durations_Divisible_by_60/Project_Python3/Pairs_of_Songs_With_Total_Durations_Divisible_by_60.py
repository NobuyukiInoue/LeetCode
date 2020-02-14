# coding: utf-8

import os
import sys
import time

class Solution:
#   def numPairsDivisibleBy60(self, time: List[int]) -> int:
    def numPairsDivisibleBy60(self, time):
        b = [0]*60
        res = 0
        for song in time:
            res += b[60 - song%60 if song%60 else 0]
            b[song%60] += 1
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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip().split(",")

    var_time = [int(val) for val in flds]
    print("time = %s" %var_time)

    time0 = time.time()

    sl = Solution()
    result = sl.numPairsDivisibleBy60(var_time)

    time1 = time.time()

    print("result = %s" %result)
    print("Execute time ... : %f[s]¥n" %(time1 - time0))

if __name__ == "__main__":
    main()
