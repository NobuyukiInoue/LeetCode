import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        # 40ms
        def helper(i: int, c: int) -> int:
            num_x_start, num_x_end = 0, 0
            other_ch = 'R' if c == 'L' else 'L'
            while i < len(start):
                if other_ch in (start[i], end[i]):
                    break
                num_x_start += (start[i] == 'X')
                num_x_end += (end[i] == 'X')
                i += 1
                if num_x_start == num_x_end:
                    return i
            return -1 
        i = 0
        while i < len(start):
            if start[i] == end[i]:
                i += 1
            else:
                j = -1
                if [start[i],end[i]] == ['X','L']:
                    j = helper(i,'L')
                elif [start[i],end[i]] == ['R', 'X']:
                    j = helper(i,'R')
                if j == -1:
                    return False
                i = j
        return True

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
    flds = temp.replace("\"","").replace(", ",",").replace("[[","").replace("]]","").rstrip().split("],[")
    v_start, v_end = flds[0], flds[1]
    print("v_start = \"{0}\", v_end = {1}".format(v_start, v_end))

    sl = Solution()
    time0 = time.time()

    result = sl.canTransform(v_start, v_end)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
