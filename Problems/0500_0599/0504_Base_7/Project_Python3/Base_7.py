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
    num = int(temp.replace("[","").replace("]","").rstrip())
    print("num = %d" %num)

    time0 = time.time()

    sl = Solution()
    result = sl.convertToBase7(num)

    print("result = %s" %result)

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
