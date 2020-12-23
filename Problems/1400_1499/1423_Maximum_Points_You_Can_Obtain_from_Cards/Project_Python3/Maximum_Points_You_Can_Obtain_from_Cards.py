# coding: utf-8

import json
import os
import sys
import time
import itertools
from typing import List, Dict, Tuple

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # 396ms
        take_from_left = [0] + [*itertools.accumulate(cardPoints[:k])]
        take_from_right = [0] + [*itertools.accumulate(reversed(cardPoints[-k:]))]
        return max(take_from_left[i] + take_from_right[k - i] for i in range(k + 1))

    def maxScore2(self, cardPoints: List[int], k: int) -> int:
        # 456ms
        cardPoints, res = cardPoints[-k:] + cardPoints[:k], 0
        for i, n in enumerate(cardPoints):
            cardPoints[i] = n + (cardPoints[i - 1] if i > 0 else 0)
        for i in range(len(cardPoints) - k + 1):
            res = max(res, cardPoints[i + k - 1] - (cardPoints[i - 1] if i > 0 else 0))
        return res

    def maxScore_bad(self, cardPoints: List[int], k: int) -> int:
        # Time Limit Exceeded.
        def dfs(start, end, k, currentTotal):
            if k == 0:
                return currentTotal
            if end < start:
                return currentTotal
            if end - start == 1:
                return currentTotal + cardPoints[start]
            sum1 = dfs(start + 1, end, k - 1, currentTotal + cardPoints[start])
            sum2 = dfs(start, end - 1, k - 1, currentTotal + cardPoints[end - 1])
            if sum1 > sum2:
                return sum1
            return sum2
        return dfs(0, len(cardPoints), k, 0)

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
    cardPoints, k = [int(n) for n in flds[0].split(",")], int(flds[1])
    print("cardPoints = {0}, k = {1}".format(cardPoints, k))

    sl = Solution()
    time0 = time.time()

    result = sl.maxScore(cardPoints, k)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
