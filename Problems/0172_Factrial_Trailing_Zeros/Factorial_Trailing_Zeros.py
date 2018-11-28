# coding: utf-8

import os
import sys
import time


class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        x, result = 5, 0
        while n >= x:
            result += n // x
            if x <= sys.maxsize / 2:
                x *= 5
            else:
                break
        return result


    def trailingZeroes_work(self, n):
        """
        :type n: int
        :rtype: int
        """
        trailingNum = 1
        for i in range(n, 1, -1):
            trailingNum *= i
        #   print("i = %d, trailingNum = %d" %(i, trailingNum))
        
        print("trailingNum = %d" %trailingNum)

        x, count = 10, 0
        while x < trailingNum:
            if trailingNum % x == 0:
                count += 1
                x *= 10
            else:
                return count
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

    time0 = time.time()

    sl = Solution()
    result = sl.trailingZeroes(n)
    print("result = %d" %result)

    time1 = time.time()

    print("Execute time ... : %f[s]" %(time1 - time0))
    print()


if __name__ == "__main__":
    main()
