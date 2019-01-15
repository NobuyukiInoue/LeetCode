# coding: utf-8

import os
import sys
import time

class Solution:
    def validMountainArray(self, A):
        if len(A) < 3 or A[0] > A[1]:
            return False

        peak_passed = False
        for i in range(1, len(A)):
            if A[i-1] == A[i]:
                return False
            elif not peak_passed and A[i-1] > A[i]:
                peak_passed = True
            elif peak_passed and A[i-1] < A[i]:
                return False
        return peak_passed

    def validMountainArray_work(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        direction, count = 1, 0
        for i in range(1, len(A)):
            if A[i] == A[i - 1]:
                return False
            if (A[i] - A[i - 1])*direction > 0:
                continue
            else:
                if count == 0 and i == 1:
                    return False
                elif count > 2:
                    return False
                count += 1
                direction *= -1
        if count == 1:
            return True
        else:
            return False

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
    result = sl.validMountainArray(A)

    print("result = %s" %result)

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
