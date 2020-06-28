# coding: utf-8

import functools
import operator
import os
import sys
import time

class Solution:
#   def numberOfSteps (self, num: int) -> int:
    def numberOfSteps (self, num):
        # 24ms
        res = 0
        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            res += 1
        return res

    def numberOfSteps2(self, num):
        # 24ms
        return len(bin(num)) + bin(num).count('1') - 3

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
    fld = temp.replace("[","").replace("]","").replace("\"","").replace(" ","")
    num = int(fld)
    
    print("num = {0:d}".format(num))

    sl = Solution()
    time0 = time.time()
    result = sl.numberOfSteps(num)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
