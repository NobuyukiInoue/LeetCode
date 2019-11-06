# coding: utf-8

import os
import sys
import time

class Solution:
#   def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    def isInterleave(self, s1, s2, s3):
        # 40ms
        l1, l2 = len(s1), len(s2)
        if l1 + l2 != len(s3):
            return False
        last = set([(0, 0)])
        for char in s3:
            current = set()
            for i, j in last:
                if i < l1 and s1[i] == char:
                    current.add((i + 1, j))
                if j < l2 and s2[j] == char:
                    current.add((i, j + 1))
            if not current:
                return False
            last = current
        return True

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip().split(",")

    s1 = flds[0]
    s2 = flds[1]
    s3 = flds[2]
    print("s1 = {0}, s2 = {1}, s3 = {2}".format(s1, s2, s3))

    time0 = time.time()

    sl = Solution()
    result = sl.isInterleave(s1, s2, s3)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
