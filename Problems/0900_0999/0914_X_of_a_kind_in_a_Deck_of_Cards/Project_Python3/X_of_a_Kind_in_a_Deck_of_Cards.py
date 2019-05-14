# coding: utf-8

import os
import sys
import time
import collections
from functools import reduce

class Solution:
#   def hasGroupsSizeX(self, deck: List[int]) -> bool:
    def hasGroupsSizeX(self, deck):
        def gcd(a, b):
            while b: a, b = b, a % b
            return a
        count = collections.Counter(deck).values()
        return reduce(gcd, count) > 1

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
    deck = str_to_int_array(flds)
    
    print("deck = %s" %deck)

    time0 = time.time()

    sl = Solution()
    result = sl.hasGroupsSizeX(deck)

    time1 = time.time()

    print("result = %s" %result)
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
