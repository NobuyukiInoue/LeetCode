import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # 31ms - 48ms
        return (1 + n)*n//2 - (1 + n//m)*(n//m)*m

    def differenceOfSums2(self, n: int, m: int) -> int:
        # 46ms - 50ms
        num1, num2 = 0, 0
        for i in range(1, n + 1):
            if i % m != 0:
                num1 += i
            else:
                num2 += i
        return num1 - num2

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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")

    n, m = int(flds[0]), int(flds[1])
    print("n = {0:d}, m = {1:d}".format(n, m))

    sl = Solution()
    time0 = time.time()

    result = sl.differenceOfSums(n, m)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
