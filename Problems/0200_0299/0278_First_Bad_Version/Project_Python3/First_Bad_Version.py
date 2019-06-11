# coding: utf-8

import os
import sys
import time

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0,n - 1
        while left <= right:
            mid = (left + right)//2
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
                
        if isBadVersion(left):
            return left
        else:
            return left + 1

def isBadVersion(n):
    if n >= 4:
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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()

    n = int(flds)
    print("n = %d" %n)

    time0 = time.time()

    sl = Solution()
    result = sl.firstBadVersion(n)

    time1 = time.time()

    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
