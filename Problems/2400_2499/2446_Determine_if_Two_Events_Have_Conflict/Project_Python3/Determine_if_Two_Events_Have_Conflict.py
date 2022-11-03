# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def haveConflict_1liner(self, event1: List[str], event2: List[str]) -> bool:
        # 33ms - 63ms
        return event1[0] <= event2[1] and event2[0] <= event1[1]

    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        # 29ms - 50ms
        t1 = (int(event1[0][0:2])*60 + int(event1[0][3:]))
        t2 = (int(event1[1][0:2])*60 + int(event1[1][3:]))
        t3 = (int(event2[0][0:2])*60 + int(event2[0][3:]))
        t4 = (int(event2[1][0:2])*60 + int(event2[1][3:]))
        if t1 > t3:
            t1, t2, t3, t4 = t3, t4, t1, t2
        if t2 >= t3:
            return True
        return False

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
    event1 = flds[0].split(",")
    event2 = flds[1].split(",")
    print("event1 = {0}, event2 = {1}".format(event1, event2))
  
    sl = Solution()
    time0 = time.time()

    result = sl.haveConflict(event1, event2)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
