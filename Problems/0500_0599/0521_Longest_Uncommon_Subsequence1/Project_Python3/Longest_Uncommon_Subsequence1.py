# coding: utf-8

import os
import sys
import time

class Solution:
#   def findLUSlength(self, a: str, b: str) -> int:
    def findLUSlength(self, a, b):
        return -1 if a == b else max(len(a), len(b))

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
    flds = temp.replace("\"","").replace(" ","").replace("[[","").replace("]]","").rstrip().split("],[")
    a = flds[0]
    b = flds[1]
    print("a = %s" %a)
    print("b = %s" %b)

    time0 = time.time()

    sl = Solution()
    result = sl.findLUSlength(a, b)

    time1 = time.time()
    print("result = %d" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
