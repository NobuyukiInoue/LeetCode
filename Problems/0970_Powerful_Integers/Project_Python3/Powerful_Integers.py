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
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    flds = temp.replace("[","").replace("]","").rstrip().split(",")
    x, y, bound = int(flds[0]), int(flds[1]), int(flds[2])

    time0 = time.time()

    sl = Solution()
    result = sl.powerfulIntegers(x, y, bound)
    print("result = %s" %result)

    time1 = time.time()

    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
