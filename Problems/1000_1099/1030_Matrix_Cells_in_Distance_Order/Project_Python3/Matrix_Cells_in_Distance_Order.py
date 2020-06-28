# coding: utf-8

import os
import sys
import time

class Solution:
#   def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
    def allCellsDistOrder(self, R, C, r0, c0):
        # 248ms
    	return sorted([(r, c) for r in range(R) for c in range(C)], key=lambda p: abs(p[0] - r0) + abs(p[1] - c0))

    def allCellsDistOrder(self, R, C, r0, c0):
        # 272ms
        counter = [0 for _ in range(R + C + 1)]
        for r in range(R):
            for c in range(C):
                dist = abs(r - r0) + abs(c - c0)
                counter[dist + 1] += 1

        for i in range(len(counter)):
            counter[i] += counter[i - 1]

        ans = [[0, 0] for _ in range(R*C)]
    #   print("counter = {0}".format(counter))
        for r in range(R):
            for c in range(C):
                dist = abs(r - r0) + abs(c - c0)
            #   print("dist = {0:d}, counter[dist] = {1:d}, (r, c) = ({2:d}, {3:d})".format(dist, counter[dist], r, c))
                ans[counter[dist]] = [r, c]
                counter[dist] += 1

        return ans

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip().split(",")
    R = int(flds[0])
    C = int(flds[1])
    r0 = int(flds[2])
    c0 = int(flds[3])
    print("R = {0:d}, C = {1:d}, r0 = {2:d}, c0 = {3:d}\n".format(R, C, r0, c0))

    sl = Solution()
    time0 = time.time()

    result = sl.allCellsDistOrder(R, C, r0, c0)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
