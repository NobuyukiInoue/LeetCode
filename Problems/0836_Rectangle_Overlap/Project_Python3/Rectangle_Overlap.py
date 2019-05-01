# coding: utf-8

import os
import sys
import time

class Solution:
#    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
    def isRectangleOverlap(self, rec1, rec2):
        return rec1[0] < rec2[2] and rec2[0] < rec1[2] and rec1[1] < rec2[3] and rec2[1] < rec1[3]

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
    flds = temp.replace("[[","").replace("]]","").replace("\"","").replace(" ","").rstrip().split("],[")

    rec1 = []*4
    pt1 = flds[0].split(",")
    rec1 = [int(pt1[0]), int(pt1[1]), int(pt1[2]), int(pt1[3])]

    rec2 = []*4
    pt2 = flds[1].split(",")
    rec2 = [int(pt2[0]), int(pt2[1]), int(pt2[2]), int(pt2[3])]

    print("rect1 = %s, rect2 = %s" %(rec1, rec2))

    time0 = time.time()

    sl = Solution()
    result = sl.isRectangleOverlap(rec1, rec2)
    print("result = %s" %result)

    time1 = time.time()

    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
