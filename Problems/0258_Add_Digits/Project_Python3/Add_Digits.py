# coding: utf-8

import os
import sys
import time


class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        return num % 9 if num % 9 != 0 else 9
    
    def addDigits_work(self, num):
        """
        :type num: int
        :rtype: int
        """
        sum, temp = 0, num
        while True:
            while True:
                sum += temp % 10
                temp //= 10
                if temp == 0:
                    break
            if sum < 10:
                break
            temp, sum = sum, 0
        return sum


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
        print("argv[1] = %s" %temp)
        loop_main(temp)


def loop_main(temp):
    num = int(temp)

    time0 = time.time()

    sl = Solution()
    result = sl.addDigits(num)
    print("result = %s" %result)

    time1 = time.time()

    print("Execute time ... : %f[s]" %(time1 - time0))
    print()


if __name__ == "__main__":
    main()
