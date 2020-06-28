# coding: utf-8

import os
import sys
import time

class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        s = set()
        stack = [(0, 0)]
        while stack:
            i, j = stack.pop()
            t = x ** i + y ** j
            if t <= bound:
                s.add(t)
                if x > 1:
                    stack.append((i + 1, j))
                if y > 1:
                    stack.append((i, j + 1))
        return list(s)

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
    flds = temp.replace("[","").replace("]","").rstrip().split(",")
    x, y, bound = int(flds[0]), int(flds[1]), int(flds[2])

    sl = Solution()
    time0 = time.time()
    result = sl.powerfulIntegers(x, y, bound)
    print("result = {0}".format(result))

    time1 = time.time()

    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
