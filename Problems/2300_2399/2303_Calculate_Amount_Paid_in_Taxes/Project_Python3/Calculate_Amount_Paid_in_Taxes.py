# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        # 95ms - 116ms
        tax = prev = 0
        for upper, p in brackets:
            if income >= upper:
                tax += (upper - prev) * p / 100
                prev = upper
            else:
                tax += (income - prev) * p / 100
                return tax
        return tax

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
    flds = temp.replace(" ","").replace("\"","").split("]],[")

    brackets = [[int(col) for col in data.split(",")] for data in flds[0].replace("[[[", "").split("],[")]
    income = int(flds[1].replace("]]", ""))
    print("brackets = {0}, income = {1}".format(brackets, income))
  
    sl = Solution()
    time0 = time.time()

    result = sl.calculateTax(brackets, income)

    time1 = time.time()

    print("result = {0:f}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
