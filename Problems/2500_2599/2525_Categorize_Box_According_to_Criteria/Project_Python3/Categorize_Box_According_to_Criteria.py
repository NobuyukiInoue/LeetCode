# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        # 29ms - 32ms
        bulky = max(length, width, height) >= 1e4 or length*width*height >= 1e9
        heavy = mass >= 100 
        if bulky and heavy:
            return "Both"
        if bulky:
            return "Bulky"
        if heavy:
            return "Heavy"
        return "Neither"

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
    flds = temp.replace("[","").replace("]","").replace(", ",",").rstrip()
    nums = [int(n) for n in flds.split(",")]
    length, width, height, mass = nums[0], nums[1], nums[2], nums[3]
    print("length = {0:d}, width = {1:d}, height = {2:d}, mass = {3:d}".format(length, width, height, mass))

    sl = Solution()

    time0 = time.time()

    result = sl.categorizeBox(length, width, height, mass)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
