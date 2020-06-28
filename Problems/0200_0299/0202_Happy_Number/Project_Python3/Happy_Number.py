# coding: utf-8

import os
import sys
import time

class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        temp = n
        flds = []
        while True:
            while True:
                flds.append(temp % 10)
                temp //= 10
                if temp == 0:
                    break
        #   print(flds)
            temp = 0
            for i in range(len(flds)):
                temp += flds[i]**2
            if temp == 1:
                print("temp = {0:d}".format(temp))
                return True
            if temp == 2:
                print("temp = {0:d}".format(temp))
                return False
            if temp == 3:
                print("temp = {0:d}".format(temp))
                return False
            if temp == 4:
                print("temp = {0:d}".format(temp))
                return False
            if temp == 5:
                print("temp = {0:d}".format(temp))
                return False
            flds.clear()

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
    n = int(temp)

    sl = Solution()
    time0 = time.time()
    result = sl.isHappy(n)
    print("result = {0:d}".format(result))

    time1 = time.time()

    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
