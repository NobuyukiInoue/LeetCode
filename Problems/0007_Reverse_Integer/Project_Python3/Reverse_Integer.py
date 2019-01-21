# coding: utf-8

import os
import sys
import time


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            result = (0 - int(str(0-x)[::-1]))
            if result <= 2147483647 and result >= -2147483648:
                return result
            else:
                return 0
        else:
            result = int(str(x)[::-1])
            if result <= 2147483647 and result >= -2147483648:
                return result
            else:
                return 0

    def reverse2(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        neg = False
        if x < 0:
            neg = True
            x = -x
        while x != 0:
            v = x % 10
            x = x / 10
            result = result * 10 + v
        if neg:
            result = -result
        return result if result >= -2147483648 and result <= 2147483647 else 0


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
    x = int(temp)

    time0 = time.time()

    sl = Solution()
    result = sl.reverse(x)
    print("result = %d" %result)

    time1 = time.time()

    print("Execute time ... : %f[s]" %(time1 - time0))
    print()


if __name__ == "__main__":
    main()
