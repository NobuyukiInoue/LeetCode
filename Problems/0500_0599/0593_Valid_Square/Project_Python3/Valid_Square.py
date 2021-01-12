# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def validSquare2(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        # 36ms
        memo = {tuple(p1), tuple(p2), tuple(p3), tuple(p4)}
        if len(memo) != 4:
            return False
        def helper(a, b):
            return (a[0] - b[0])**2 + (a[1] - b[1])**2
        return helper(p1, p3) == helper(p2, p4) and helper(p1, p4) == helper(p2, p3) and helper(p1, p2) == helper(p3, p4) and (helper(p1, p4) == helper(p1, p2) or helper(p1, p4) == helper(p1, p3) or helper(p1, p2) == helper(p1, p3))

    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        # 36ms
        array = [p1, p2, p3, p4]
        edge_length = []
        for i in range(len(array)):
            for j in range(i + 1,len(array)):
                edge_length.append(pow(array[i][0] - array[j][0], 2) + pow(array[i][1] - array[j][1], 2))
        edge_length.sort()

        def check(array):
            for i in range(4):
                if array[i] == 0:
                    return False
                if array[i] != array[0]:
                    return False
            for i in range(4, len(array)):
                if array[i] == 0:
                    return False
                if array[i] != array[4]:
                    return False
            return array[0]*2 == array[4]

        return check(edge_length)

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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip()

    points = flds.split("],[")
    p1 = [int(n) for n in points[0].split(",")]
    p2 = [int(n) for n in points[1].split(",")]
    p3 = [int(n) for n in points[2].split(",")]
    p4 = [int(n) for n in points[3].split(",")]
    print("p1 = {0}".format(p1))
    print("p2 = {0}".format(p2))
    print("p3 = {0}".format(p3))
    print("p4 = {0}".format(p4))
  
    sl = Solution()
    time0 = time.time()

    result = sl.validSquare(p1, p2, p3, p4)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
