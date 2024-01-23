import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        # 41ms - 49ms
        if a == e and not (a == c and d > min(b,f) and d < max(b,f)):
            return 1
        if b == f and not (b == d and c > min(a,e) and c < max(a,e)):
            return 1
        if c + d == e + f and not (c + d == a + b and a > min(c , e) and a < max(c, e)):
            return 1
        if c - d == e-f and not (c - d == a - b and a > min(c , e) and a < max(c, e)):
            return 1
        return 2

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

    a, b, c, d, e, f = int(flds[0]), int(flds[1]), int(flds[2]), int(flds[3]), int(flds[4]), int(flds[5])
    print("a = {0:d}, b = {1:d}, c = {2:d}, d = {3:d}, e = {4:d}, f = {5:d}".format(a, b, c, d, e, f))

    sl = Solution()
    time0 = time.time()

    result = sl.minMovesToCaptureTheQueen(a, b, c, d, e, f)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
