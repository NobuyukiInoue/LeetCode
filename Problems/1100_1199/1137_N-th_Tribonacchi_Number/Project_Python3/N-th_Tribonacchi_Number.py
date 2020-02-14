# coding: utf-8

import os
import sys
import time

class Solution:
#   def tribonacci(self, n: int) -> int:
    def tribonacci(self, n):
        # 36ms
        if n == 0:
            return 0
        if n <= 2:
            return 1
        t0, t1, t2 = 0, 1, 1
        for i in range(3, n + 1):
            t0, t1, t2 = t1, t2, t0 + t1 + t2
        return t2

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()
    n = int(flds)
    print("n = {0}".format(n))
    time0 = time.time()

    sl = Solution()
    result = sl.tribonacci(n)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
