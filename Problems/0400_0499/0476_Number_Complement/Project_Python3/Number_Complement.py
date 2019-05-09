# coding: utf-8

import math
import os
import sys
import time

class Solution:
#    def findComplement(self, num: int) -> int:
    def findComplement(self, num):
        temp = "0b"
        binf = bin(num)
        binf = binf[2:]
        for i in list(binf):
            j = int(i)^1
            temp += format(int(i)^1)
        return int(temp, 2)

#    def findComplement(self, num: int) -> int:
    def findComplement2(self, num):
        res, t = 0, 1
        while num > 0:
            res += t*((num % 2 + 1) % 2)
            t *= 2
            num //= 2
        return res

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
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    flds = temp.replace("\"","").replace(" ","").replace("[","").replace("]","").rstrip()
    num = int(flds)

    print("num = %d" %num)

    time0 = time.time()

    sl = Solution()
    result = sl.findComplement(num)

    time1 = time.time()

    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
