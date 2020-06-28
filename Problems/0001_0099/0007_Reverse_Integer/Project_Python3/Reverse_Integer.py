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

    if argc < 2:
        print("Usage: python {0} <testdata.txt>".format(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("{0} not found...".format(argv[1]))
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        temp = temp.strip()
        if temp == "":
            continue
        print("args = {0}".format(temp))
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    x = int(temp)

    sl = Solution()
    time0 = time.time()

    result = sl.reverse(x)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
