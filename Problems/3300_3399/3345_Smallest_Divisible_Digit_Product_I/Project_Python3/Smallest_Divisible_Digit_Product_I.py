import functools
import operator
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        # 0ms
        def getProd(n: int) -> int:
            prod = 1
            while n > 0:
                prod *= n%10
                n //= 10
            return prod

        while True:
            if getProd(n)%t == 0:
                return n
            n += 1

    def smallestNumber2(self, n: int, t: int) -> int:
        # 0ms
        for i in range(n, n + 10):
            if functools.reduce(operator.mul, map(int,str(i))) %t == 0:
                return i

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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    
    n, t = int(flds[0]), int(flds[1])
    print("n = {0:d}, t = {1:d}".format(n, t))

    sl = Solution()
    time0 = time.time()

    result = sl.smallestNumber(n, t)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
