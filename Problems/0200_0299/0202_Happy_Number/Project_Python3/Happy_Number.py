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
                print("temp = %d" %temp)
                return True
            if temp == 2:
                print("temp = %d" %temp)
                return False
            if temp == 3:
                print("temp = %d" %temp)
                return False
            if temp == 4:
                print("temp = %d" %temp)
                return False
            if temp == 5:
                print("temp = %d" %temp)
                return False
            flds.clear()


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


def loop_main(temp):
    n = int(temp)

    time0 = time.time()

    sl = Solution()
    result = sl.isHappy(n)
    print("result = %d" %result)

    time1 = time.time()

    print("Execute time ... : %f[s]" %(time1 - time0))
    print()


if __name__ == "__main__":
    main()
