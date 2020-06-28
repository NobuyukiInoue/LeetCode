# coding: utf-8

import os
import math
import sys
import time

class Solution:
#   def numPrimeArrangements(self, n: int) -> int:
    def numPrimeArrangements(self, n):
        # 36ms
        primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,
            43,47,53,59,61,67,71,73,79,83,89,97]

        modulo = int(math.pow(10,9)) + 7
        result, primeCount = 1, 0
        for target in primes:
            if target <= n:
                primeCount += 1
            else:
                break
        for i in range(2, primeCount + 1):
            result = (result*i)%modulo
        for i in range(2, (n - primeCount) + 1):
            result = (result*i)%modulo

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()
    n = int(flds)
    print("n = {0}".format(n))
    sl = Solution()
    time0 = time.time()
    result = sl.numPrimeArrangements(n)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
