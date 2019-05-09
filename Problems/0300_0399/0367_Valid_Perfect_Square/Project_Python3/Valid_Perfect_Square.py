# coding: utf-8

import os
import sys
import time


class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        high, low, mid = 46340, 0, 0
        while low <= high:
            mid = low + (high - low)//2
            if mid*mid > num:
                high = mid - 1
            elif mid*mid < num:
                low = mid + 1
            else:
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
    num = int(temp)

    time0 = time.time()

    sl = Solution()
    result = sl.isPerfectSquare(num)
    print("result = %s" %result)

    time1 = time.time()

    print("Execute time ... : %f[s]" %(time1 - time0))
    print()


if __name__ == "__main__":
    main()
