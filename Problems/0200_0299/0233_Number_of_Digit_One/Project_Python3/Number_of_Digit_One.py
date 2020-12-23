import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def countDigitOne(self, n: int) -> int:
        # 28ms
        length = len(str(n))
        result, group_size, devider = 0, 1, 10
        for i in range(1, length + 1):
            this_wei = (n//devider)*group_size + min(group_size, max(0, (n%devider) - group_size + 1))
            result += this_wei
            group_size *= 10
            devider *= 10
        return result

    def countDigitOne2(self, n: int) -> int:
        # 32ms
        return sum((n//m+8)//10*m + (n//m%10==1)*(n%m+1) for m in (10**i for i in range(10)))

    def countDigitOne3(self, n, m=1, r=1):
        # 36ms
        return int(n>0 and (n+8)//10*m + (n%10==1)*r + self.countDigitOne(n//10, m*10, r+n%10*m))

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

    result = sl.countDigitOne(n)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
