import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def sumOfMultiples(self, n: int) -> int:
        # 78ms - 82ms
        return sum(i for i in range(n + 1) if i % 3 == 0 or i % 5 == 0 or i % 7 == 0)

    def sumOfMultiples2(self, n: int) -> int:
        # 76ms - 84ms
        res = 0
        for i in range(n + 1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                res += i
        return res

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
    fld = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    n = int(fld)
    print("n = {0:d}".format(n))

    sl = Solution()
    time0 = time.time()

    result = sl.sumOfMultiples(n)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
