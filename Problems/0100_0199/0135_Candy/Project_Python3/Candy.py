# coding: utf-8

import functools
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def candy1(self, ratings: List[int]) -> int:
        # 6677ms
        return sum(map(max, functools.reduce(lambda y, x: y + [y[-1]*(x > 0) + 1], d := [*map(sub, ratings[1:], ratings)], [1]), functools.reduce(lambda y, x: y + [y[-1]*(x < 0) + 1], d[::-1],[1])[::-1]))

    def candy(self, ratings: List[int]) -> int:
        # 148ms
        candies = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                candies[i] = candies[i + 1] + 1
        return sum(candies)

    def candy_bad(self, ratings: List[int]) -> int:
        len_ratings = len(ratings)
        candies = [1 for rate in ratings]
        for i, _ in enumerate(ratings):
            if i == 0:
                if ratings[i] > ratings[i + 1]:
                    candies[i] = candies[i + 1] + 1
            elif i == len_ratings - 1:
                if ratings[i - 1] < ratings[i]:
                    candies[i] = candies[i - 1]
            else:
                if ratings[i - 1] < ratings[i] or ratings[i] > ratings[i + 1]:
                    candies[i] = max(candies[i - 1], candies[i + 1])
        return sum(candies)

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

    ratings = [int(n) for n in flds.split(",")]
    print("ratings = {0}".format(ratings))

    sl = Solution()

    time0 = time.time()

    result = sl.candy(ratings)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
