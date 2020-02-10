# coding: utf-8

import os
import sys
import time
from collections import Counter as cnt

class Solution:
#   def removeKdigits(self, num: str, k: int) -> str:
    def removeKdigits(self, num, k):
        # 32ms
        out = []
        for d in num:
            while k and out and out[-1] > d:
                out.pop()
                k -= 1
            out.append(d)
        return ''.join(out[:-k or None]).lstrip('0') or '0'


def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
        print("Usage: python %s <testdata.txt>" %(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("%s not found..." %argv[1])
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        temp = temp.strip()
        if temp == "":
            continue
        print("args = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    flds = temp.replace("[[","").replace("]]","").replace("\"","").replace(" ","").rstrip().split("],[")

    num, k = flds[0], int(flds[1])
    print("num = {0}, k = {1:d}".format(num, k))

    sl = Solution()

    time0 = time.time()

    result = sl.removeKdigits(num, k)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
