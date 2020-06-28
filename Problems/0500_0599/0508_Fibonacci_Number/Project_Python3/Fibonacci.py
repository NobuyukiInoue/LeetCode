# coding: utf-8

import os
import sys
import time

class Solution:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        if N == 1:
            return 1
        if N == 2:
            return 1
        f_n1, f_n2 = 1, 1
        for i in range(2, N):
            f_n = f_n1 + f_n2
            f_n1 = f_n2
            f_n2 = f_n
        return f_n

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
    N = int(temp.replace("[","").replace("]","").rstrip())

    sl = Solution()
    time0 = time.time()
    result = sl.fib(N)
    print("result = {0}".format(result))

    time1 = time.time()
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
