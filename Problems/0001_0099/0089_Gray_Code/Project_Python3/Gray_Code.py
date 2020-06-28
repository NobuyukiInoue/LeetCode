# coding: utf-8

import os
import sys
import time

class Solution:
#   def grayCode(self, n: int) -> List[int]:
    def grayCode(self, n):
        # 32ms
        def changeOne(n):
            if n == 0:
                return [0]
            elif n == 1:
                return [0, 1]
            else:
                subset = changeOne(n - 1)
                return subset + [2**(n - 1)+subset[i] for i in range(len(subset) - 1, -1, -1)]
        return changeOne(n)

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
    fld = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()
    n = int(fld)

    sl = Solution()
    time0 = time.time()

    result = sl.grayCode(n)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
