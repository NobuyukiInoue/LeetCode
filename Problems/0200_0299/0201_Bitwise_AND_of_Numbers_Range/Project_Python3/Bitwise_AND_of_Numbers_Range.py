# coding: utf-8

import os
import sys
import time

class Solution:
#   def rangeBitwiseAnd(self, m: int, n: int) -> int:
    def rangeBitwiseAnd(self, m, n):
        # 64ms
        shift = 0
        while m and m != n:
            m >>= 1
            n >>= 1
            shift += 1
        return m << shift

    def rangeBitwiseAnd_bad(self, m, n):
        x = m
        for i in range(m + 1, n + 1):
            x = x & i
        return x

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip().split(",")

    m = int(flds[0])
    n = int(flds[1])
    print("m = {0:d}, n = {1:d}".format(m, n))

    time0 = time.time()

    sl = Solution()
    result = sl.rangeBitwiseAnd(m, n)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
