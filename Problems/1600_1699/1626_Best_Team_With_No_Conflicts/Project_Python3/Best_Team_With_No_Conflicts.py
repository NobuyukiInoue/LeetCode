# coding: utf-8

import bisect
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        # 296ms
        new_list = sorted(zip(ages, scores))
        visited = [new_list[0][1]]
        dp = [new_list[0][1]]
        ans = new_list[0][1] 
        for i in range(1,len(new_list)):
            s = new_list[i][1]
            index = bisect.bisect_right(visited, s)
            curr = max(dp[:index]) + s if index else s
            ans = max(ans, curr)
            visited.insert(index, s)
            dp.insert(index,curr)
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
    flds = temp.replace("[[","").replace("]]","").replace("\"","").replace(" ","").rstrip().split("],[")
    scores = [int(n) for n in flds[0].split(",")]
    ages = [int(n) for n in flds[1].split(",")]
    print("scores = {0}".format(scores))
    print("ages = {0}".format(ages))

    sl = Solution()

    time0 = time.time()

    result = sl.bestTeamScore(scores, ages)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
