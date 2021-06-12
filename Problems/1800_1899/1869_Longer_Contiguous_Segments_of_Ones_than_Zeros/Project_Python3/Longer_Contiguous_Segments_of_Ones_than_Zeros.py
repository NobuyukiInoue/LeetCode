import operator
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        # 20ms
        return operator.gt(*(max(map(len, s.split(b))) for b in '01'))

    def checkZeroOnes2(self, s: str) -> bool:
        # 24ms
        return max(len(x) for x in s.split('0')) > max(len(x) for x in s.split('1'))

    def checkZeroOnes3(self, s: str) -> bool:
        # 28ms
        c0, c1, max_c0, max_c1 = 0, 0, 0, 0
        for ch in s:
            if ch == "1":
                c0 = 0
                c1 += 1
                max_c1 = max(max_c1, c1)
            else:
                c1 = 0
                c0 += 1
                max_c0 = max(max_c0, c0)
        return max_c1 > max_c0

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
    s = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    print("s = {0}".format(s))

    sl = Solution()
    time0 = time.time()

    result = sl.checkZeroOnes(s)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
