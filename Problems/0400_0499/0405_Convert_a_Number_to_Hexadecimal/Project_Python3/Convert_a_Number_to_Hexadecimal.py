# coding: utf-8

import os
import sys
import time

class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        resultStr = ""

        if num > 0:
            temp = num
        elif num == 0:
            return "0"
        else:
            temp = 2**32 + num

        while temp > 0:
            modded = temp % 16
            resultStr = chars[modded] + resultStr
            temp //= 16
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
    num = int(temp)

    sl = Solution()
    time0 = time.time()
    result = sl.toHex(num)
    print("result = {0}".format(result))

    time1 = time.time()

    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
