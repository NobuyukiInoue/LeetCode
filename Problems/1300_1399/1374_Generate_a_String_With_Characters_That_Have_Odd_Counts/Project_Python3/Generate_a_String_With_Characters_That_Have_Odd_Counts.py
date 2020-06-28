# coding: utf-8

import collections
import os
import sys
import time

class Solution:
#   def generateTheString(self, n: int) -> str:
    def generateTheString1(self, n):
        return 'b' + 'ab'[n & 1] * (n - 1)

    def generateTheString(self, n):
        # 24ms
        if n % 2 == 1:
            return 'a'*n
        else:
            return 'a'*(n - 1) + 'b'

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()

    n = int(flds)
    print("n = {0}".format(n))

    sl = Solution()
    time0 = time.time()
    result = sl.generateTheString(n)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
