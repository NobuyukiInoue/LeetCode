# coding: utf-8

import os
import sys
import time

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
    #   print("n = {0:d}, {1}".format(n, bin(n)))
        for i in range(0,32):
            result = result*2 + n%2
            n //= 2
        #   print("result = {0}, n = {1}".format(bin(result), bin(n)))
        
        return result

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
    flds = temp.replace("[", "").replace("]", "").rstrip()

    n = int(flds)
    print("n = {0:d}".format(n))
    print("{0}".format(format(n, '#032b')))

    sl = Solution()
    time0 = time.time()

    result = sl.reverseBits(n)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("{0}".format(format(result, '#032b')))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
