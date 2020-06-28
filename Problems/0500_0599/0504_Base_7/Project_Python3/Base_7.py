# coding: utf-8

import os
import sys
import time

class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        resultStr = ""

        if num == 0:
            return "0"
        elif num > 0:
            isNegative = False
        else:
            isNegative = True
            num = -num

        while num > 0:
            resultStr = str(num % 7) + resultStr
            num //= 7

        if isNegative:
            return "-" + resultStr
        else:
            return resultStr

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
    num = int(temp.replace("[","").replace("]","").rstrip())
    print("num = {0:d}".format(num))

    sl = Solution()
    time0 = time.time()
    result = sl.convertToBase7(num)

    print("result = {0}".format(result))

    time1 = time.time()
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
