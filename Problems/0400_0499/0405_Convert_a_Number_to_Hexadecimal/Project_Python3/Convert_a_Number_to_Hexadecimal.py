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
    num = int(temp)

    time0 = time.time()

    sl = Solution()
    result = sl.toHex(num)
    print("result = %s" %result)

    time1 = time.time()

    print("Execute time ... : %f[s]" %(time1 - time0))
    print()


if __name__ == "__main__":
    main()
