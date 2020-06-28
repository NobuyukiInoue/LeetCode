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
    num = int(temp)

    sl = Solution()
    time0 = time.time()
    result = sl.addDigits(num)
    print("result = {0}".format(result))

    time1 = time.time()

    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
