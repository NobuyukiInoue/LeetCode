import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def isFascinating(self, n: int) -> bool:
        # 41ms - 52ms
        cnts = collections.defaultdict(bool)
        arr = [n, 2*n, 3*n]
        for cur in arr:
            temp = cur
            while temp > 0:
                if cnts[temp % 10] or temp%10 == 0:
                    return False
                cnts[temp % 10] = True
                temp //= 10
        return True

    def isFascinating_1liner1(self, n: int) -> bool:
        # 47ms - 53ms
        return n in {192, 219, 273, 327}

    def isFascinating_1liner2(self, n: int) -> bool:
        # 50ms - 57ms        
        return ''.join(sorted(str(n) + str(2*n) + str(3*n))) == '123456789'

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

    result = sl.isFascinating(n)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
