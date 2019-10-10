# coding: utf-8

import os
import sys
import time
import copy

class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = s.rstrip()
        if len(temp) == 0:
            return 0
        while temp.find("  ") >= 0:
            temp = temp.replace("  ", " ")
        return len(temp.strip().split(" "))


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
    #    print("Hit Return to continue...")
    #    input()


def loop_main(temp):
    var_str = temp.replace("\"","").rstrip()

    print("s = %s" %var_str)

    time0 = time.time()

    sl = Solution()
    result = sl.countSegments(var_str)

    print("result = %s" %result)

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()


if __name__ == "__main__":
    main()
