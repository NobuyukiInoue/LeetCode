# coding: utf-8

import collections
import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        # 48ms
        res = cur = 0
        d = collections.deque(sorted(tokens))
        while d and (d[0] <= P or cur):
            if d[0] <= P:
                P -= d.popleft()
                cur += 1
            else:
                P += d.pop()
                cur -= 1
            res = max(res, cur)
        return res

    def bagOfTokensScore2(self, tokens: List[int], P: int) -> int:
        # 48ms
        n = len(tokens)
        if n == 0:
            return 0
        tokens.sort()
        if P < tokens[0]:
            return 0
        i, j, score, m1 = 0, n - 1, 0, 0
        while i <= j:
            if P >= tokens[i]:
                score += 1
                P -= tokens[i]
                i += 1
                m1 = max(m1, score)
            elif score > 0:
                P += tokens[j]
                j -= 1
                score -= 1
        return m1

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
    tokens = [int(n) for n in flds[0].split(",")]
    P = int(flds[1])
    print("tokens = {0}, P = {1:d}".format(tokens, P))

    sl = Solution()

    time0 = time.time()

    result = sl.bagOfTokensScore(tokens, P)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
