# coding: utf-8

import collections
import os
import re
import sys
import time

class Solution:
#   def maxScore(self, s: str) -> int:
    def maxScore(self, s):
        # 36ms
        return max([s[:i].count('0') + s[i:].count('1') for i in range(1, len(s))])


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
    s = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()

    sl = Solution()
    time0 = time.time()

    result = sl.maxScore(s)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
