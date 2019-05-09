# coding: utf-8

import os
import sys
import time

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count('1')

    def hammingDistance_work(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        counts = 0
        while x > 0 or y > 0:
            if x % 2 != y % 2:
                counts += 1
            x //= 2
            y //= 2
        return counts

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
    flds = temp.replace("[","").replace("]","").rstrip().split(",")
    x = int(flds[0])
    y = int(flds[1])

    time0 = time.time()

    sl = Solution()
    result = sl.hammingDistance(x, y)

    print("result = %s" %result)

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
