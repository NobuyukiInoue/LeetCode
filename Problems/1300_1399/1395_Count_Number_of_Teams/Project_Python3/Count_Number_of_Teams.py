# coding: utf-8

import bisect
import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        # 168ms
        l, r, result = [], sorted(rating), 0
        for num in rating:
            i, j = bisect.bisect_left(l, num), bisect.bisect_right(r, num)
            result += i * (len(r) - j) + (len(l) - i) * (j - 1)
            l, r = l[ : i] + [num] + l[i : ], r[ : j - 1] + r[j : ]
        return result

    def numTeams2(self, rating: List[int]) -> int:
        # 984ms
        arr_asc, arr_desc = [0]*len(rating), [0]*len(rating)
        ans = 0
        for i, _ in enumerate(rating):
            for j in range(0, i):
                if rating[i] > rating[j]:
                    arr_desc[i] += 1
                    ans += arr_desc[j]
                elif rating[i] < rating[j]:
                    arr_asc[i] += 1
                    ans += arr_asc[j]
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
    flds = temp.replace("[", "").replace("]", "").replace(", ", ",").rstrip()

    rating = [int(n) for n in flds.split(",")]
    print("rating = {0}".format(rating))

    sl = Solution()

    time0 = time.time()

    result = sl.numTeams(rating)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
