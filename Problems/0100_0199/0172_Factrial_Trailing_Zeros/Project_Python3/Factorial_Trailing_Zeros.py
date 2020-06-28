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
        #   print("i = {0:d}, trailingNum = {1:d}".format(i, trailingNum))
        
        print("trailingNum = {0:d}".format(trailingNum))

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
    str_args = temp.replace("\"","").replace("[","").replace("]","").rstrip()

    n = int(str_args)
    print("n = {0}".format(n))

    sl = Solution()
    time0 = time.time()
    result = sl.trailingZeroes(n)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
