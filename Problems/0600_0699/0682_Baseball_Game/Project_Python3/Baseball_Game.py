# coding: utf-8

import os
import sys
import time

class Solution:
#    def calPoints(self, ops: List[str]) -> int:
    def calPoints(self, ops):
        points = []
        for cur in ops:
            if cur == "C":
                points.pop()
            elif cur == "D":
                points.append(2*points[-1])
            elif cur == "+":
                points.append(points[-1] + points[-2])
            else:
                points.append(int(cur))
        return sum(points)

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
    ops = temp.replace("\"","").replace(" ","").replace("[","").replace("]","").rstrip().split(",")
    print("ops = {0}".format(ops))

    sl = Solution()
    time0 = time.time()

    result = sl.calPoints(ops)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
