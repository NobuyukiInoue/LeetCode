# coding: utf-8

import os
import sys
import time
from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        k = sorted(list(permutations(A)), reverse=True)
        for i in k:            
            a,b,c,d = i
            su = (a*10 + b)
            sd = (c*10 + d) 
            if su < 24 and sd <60:
                return  f"{a}{b}:{c}{d}"
        return ''

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
        print("argv[1] = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    flds = temp.replace("[","").replace("]","").rstrip().split(",")
    A = str_to_int_array(flds)

    time0 = time.time()

    sl = Solution()
    result = sl.largestTimeFromDigits(A)

    print("result = %s" %result)

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
