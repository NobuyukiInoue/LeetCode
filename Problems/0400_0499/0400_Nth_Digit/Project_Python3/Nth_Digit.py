# coding: utf-8

import os
import sys
import time

class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n or n < 0:
            return 0

        up_bound = 9
        i = 1
        while n > up_bound:
            i += 1
            up_bound += i * 9 * 10 ** (i - 1)
        low_bound = up_bound - i * 9 * 10 ** (i - 1)
        # now i is the number of digits of this number num

        num = 10 ** (i - 1) + (n - 1 - low_bound) // i
        nth = (n - 1 - low_bound) % i

        return (num // 10 ** (i - 1 - nth)) % 10

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
    flds = temp.replace("[","").replace("]","")
    n = int(flds)

    print("n = {0:d}".format(n))
    sl = Solution()
    time0 = time.time()
    result = sl.findNthDigit(n)
    print("result = {0}".format(result))

    time1 = time.time()

    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
