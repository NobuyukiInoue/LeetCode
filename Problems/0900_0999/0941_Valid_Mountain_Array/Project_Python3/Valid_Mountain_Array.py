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
    flds = temp.replace("[","").replace("]","").rstrip()

    A = [int(n) for n in flds.split(",")]
    time0 = time.time()

    sl = Solution()
    result = sl.validMountainArray(A)

    time1 = time.time()

    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
