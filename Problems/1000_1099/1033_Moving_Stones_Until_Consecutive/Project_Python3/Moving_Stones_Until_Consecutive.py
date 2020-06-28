# coding: utf-8

import os
import sys
import time

class Solution:
#   def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
    def numMovesStones(self, a, b, c):
        ret = [0]*2
        input = [0]*3
        input[2] = max(a, b, c)
        input[0] = min(a, b, c)
        input[1] = a + b + c - input[2] - input[0]

        if input[2] - input[1] == input[1] - input[0] and input[1] - input[0] == 1:
            ret[0] = 0
            ret[1] = 0
            return ret

        if input[2] - input[1] > input[1] - input[0]:
            tmp = input[1] - input[0]
        else:
            tmp = input[2] - input[1]

        if tmp <= 2:
            ret[0] = 1
        else:
            ret[0] = 2

        ret[1] = input[2] - input[1] - 1 + input[1] - input[0] - 1

        return ret

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
    a = int(flds[0])
    b = int(flds[1])
    c = int(flds[2])
    print("a = {0:d}, b = {1:d}, c = {2:d}".format(a, b, c))

    sl = Solution()
    time0 = time.time()

    result = sl.numMovesStones(a, b, c)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
