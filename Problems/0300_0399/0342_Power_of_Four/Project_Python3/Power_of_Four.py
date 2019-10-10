# coding: utf-8

import os
import sys
import time


class Solution:
    def isPowerOfFour(self, num: 'int') -> 'bool':
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        
        while True:
            if num == 1:
                return True
            elif num % 4 != 0:
                return False
            num //= 4

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
    flds = temp.replace("[","").replace("]","")
    num = int(flds)

    print("num = %d" %num)
    time0 = time.time()

    sl = Solution()
    result = sl.isPowerOfFour(num)
    print("result = %s" %result)

    time1 = time.time()

    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
