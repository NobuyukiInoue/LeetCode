# coding: utf-8

import math
import os
import sys
import time

class Solution:
#    def judgeSquareSum(self, c: int) -> bool:
    def judgeSquareSum(self, c):
        for a in range(int(math.sqrt(c / 2)) + 1):
            if math.sqrt(c - a ** 2).is_integer():
                return True
        return False

def main():
    argv = sys.argv
    argc = len(argv)

    if (argc < 2):
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


def loop_main(temp):
    flds = temp.replace("[","").replace("]","").rstrip()
    c = int(flds)

    time0 = time.time()

    sl = Solution()
    result = sl.judgeSquareSum(c)
    print("result = %s" %result)

    time1 = time.time()

    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
