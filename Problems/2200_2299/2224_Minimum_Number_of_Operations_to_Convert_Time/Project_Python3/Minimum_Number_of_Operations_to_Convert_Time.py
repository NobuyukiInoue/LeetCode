# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        # 28ms - 42ms
        v1, v2 = current.split(":"), correct.split(":")
        minutes = (int(v2[0])*60 + int(v2[1])) - (int(v1[0])*60 + int(v1[1]))
        ans, ops = 0, [60, 15, 5, 1]
        for op in ops:
            ans += minutes // op
            minutes %= op
        return ans

    def convertTime_oneliner(self, current: str, correct: str) -> int:
        # 38ms - 57ms
        return ((lambda x : (x[2] - x[0])+ (x[3]-x[1])//15 + ((x[3]-x[1])%15)//5 + ((x[3]-x[1])%15)%5)((lambda a, b, c, d  : [a, b, c-1, d+60] if d < b else [a, b, c, d])(int(current.split(':')[0]), int(current.split(':')[1]),int(correct.split(':')[0]), int(correct.split(':')[1]))))

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
    flds = temp.replace(" ","").replace("\"","").replace("[","").replace("]","").rstrip()

    clocks = flds.split(",")
    current, correct = clocks[0], clocks[1]
    print("current = {0}, correct = {1}".format(current, correct))
  
    sl = Solution()
    time0 = time.time()

    result = sl.convertTime(current, correct)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
