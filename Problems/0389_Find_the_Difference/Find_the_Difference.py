# coding: utf-8

import os
import sys
import time


class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        str='abcdefghijklmnopqrstuvwxyz'
        for item in str:
            if len(s.split(item))!=len(t.split(item)):
                return item
    

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
    flds = temp.split(",")
    s = flds[0]
    t = flds[1]

    time0 = time.time()

    sl = Solution()
    result = sl.findTheDifference(s, t)
    print("result = %s" %result)

    time1 = time.time()

    print("Execute time ... : %f[s]" %(time1 - time0))
    print()


if __name__ == "__main__":
    main()
