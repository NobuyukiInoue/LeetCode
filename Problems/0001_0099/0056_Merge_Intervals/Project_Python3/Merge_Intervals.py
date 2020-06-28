# coding: utf-8

import copy
import os
import sys
import time

class Solution:
#   def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    def merge(self, intervals):
        # 88ms
        intervals = sorted(intervals)
        current_left_bound = None
        current_right_bound = None
        res = []
        
        for l, r in intervals:
            if current_left_bound is None:
                current_left_bound, current_right_bound = l, r
            else:
                if current_left_bound <= l <= current_right_bound:
                    current_right_bound = max(current_right_bound, r)
                else:
                    res.append([current_left_bound, current_right_bound])
                    current_left_bound = l
                    current_right_bound = r
        
        if current_left_bound is not None:
            res.append([current_left_bound, current_right_bound])
        
        return res

    def merge2(self, intervals):
        # 92-104ms
        ret = []
        for l, r in sorted(intervals):
            if ret and ret[-1][1] >= l:
                ret[-1] = [ret[-1][0], max(ret[-1][1], r)]
            else:
                ret.append([l, r])
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
    flds = temp.replace("\"","").replace(" ","").replace("[[","").replace("]]","").rstrip().split("],[")

    data0 = flds[0].split(",")
    intervals = [[0 for j in range(len(data0))] for i in range(len(flds))]

    for i in range(len(flds)):
        line = flds[i].split(",")
        for j in range(len(line)):
            intervals[i][j] = int(line[j])
    print("intervals = {0}".format(intervals))

    sl = Solution()
    time0 = time.time()

    result = sl.merge(intervals)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
