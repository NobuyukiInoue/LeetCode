# coding: utf-8

import os
import sys
import time

class Solution:
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """ 
        count = 0
        for i in range(0, 32):
            if n % 2 == 1:
                count += 1
            n = n // 2
        
        return count

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

def loop_main(temp):
    n = int(temp)
    print("n = %s" %n)
    print("%s" %format(n, '#032b'))

    time0 = time.time()

    sl = Solution()
    result = sl.hammingWeight(n)

    time1 = time.time()

    print("result = %d" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
