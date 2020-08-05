# coding: utf-8

import os
import operator
import sys
import time

class Solution:
#   def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
    def numWaterBottles(self, numBottles, numExchange):
        # 36ms
        exchangedBottles = 0
        while numBottles >= numExchange:
            divBottles = numBottles // numExchange
            exchangedBottles += divBottles*numExchange
            numBottles = numBottles % numExchange + divBottles
        return exchangedBottles + numBottles

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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    numBottles, numExchange = int(flds[0]), int(flds[1])
    print("numBottles = {0:d}, numExchange = {1:d}".format(numBottles, numExchange))

    sl = Solution()
    time0 = time.time()

    result = sl.numWaterBottles(numBottles, numExchange)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
