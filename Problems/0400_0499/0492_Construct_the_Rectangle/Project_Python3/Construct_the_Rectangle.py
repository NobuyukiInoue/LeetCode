# coding: utf-8

import math
import os
import sys
import time

class Solution:
#    def constructRectangle(self, area: int) -> List[int]:
    def constructRectangle(self, area):
        mid = int(math.sqrt(area))
        while area%mid != 0:
            mid -= 1
        return [area//mid, mid]


#    def constructRectangle(self, area: int) -> List[int]:
    def constructRectangle2(self, area):
        sq = math.sqrt(area)
        int_sq = int(sq)
        if sq == int_sq:
            return [int_sq, int_sq]

        H, W = 0, 0
        min = sys.maxsize
        for i in range(1, int_sq + 1):
            j = area // i
            if i * j == area:
                if j - i < min:
                    min = j - i
                    W = i
                    H = j
        return [H, W]

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
    flds = temp.replace("\"","").replace(" ","").replace("[","").replace("]","").rstrip()

    area = int(flds)
    print("area = {0:d}".format(area))

    sl = Solution()
    time0 = time.time()

    result = sl.constructRectangle(area)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
