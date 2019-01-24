# coding: utf-8

import os
import sys
import time

class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        squareA = [0]*len(A)
        for i in range(len(A)):
            squareA[i] = A[i]**2
        squareA.sort()
        return squareA

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
        print("argv[1] = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    flds = temp.replace("[","").replace("]","").rstrip()
    A = str_to_int_array(flds)

    time0 = time.time()

    sl = Solution()
    result = sl.sortedSquares(A)
    print("result = %s" %result)

    time1 = time.time()

    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
