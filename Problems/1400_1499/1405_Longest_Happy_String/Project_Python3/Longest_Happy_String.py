# coding: utf-8

import os
import sys
import time
import heapq
from typing import List, Dict, Tuple

class Solution:
    def longestDiverseString2(self, a: int, b: int, c: int) -> str:
        # 28ms
        letters = ["a"*a, "b"*b, "c"*c]
        letters.sort(key=lambda s: -len(s))
        res = []
        while any(s for s in letters):
            if (not res and letters[0] or
                    res and letters[0] and letters[0][0] != res[-1][0]):
                res.append(letters[0][:2])
                letters[0] = letters[0][2:]
            elif res and letters[1] and letters[1][0] != res[-1][0]:
                if len(letters[0]) == len(letters[1]):
                    res.append(letters[1][:2])
                    letters[1] = letters[1][2:]
                else:
                    res.append(letters[1][:1])
                    letters[1] = letters[1][1:]
            else:
                break
            letters.sort(key=lambda s: -len(s))
        return "".join(res)

    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # 24ms
        count = [[-a, 'a'],[-b, 'b'],[-c, 'c']]
        heapq.heapify(count)
        ans = [(None, None)]
        while count:
            tval, tchar = heapq.heappop(count)
            sval, schar = 0, 0
            if len(count) > 0:
                sval,schar = heapq.heappop(count)
            tadd = min(2, -tval)
            tval += tadd
            if tchar == ans[-1][0] and len(ans[-1]) + tadd >= 3:
                break
            ans.extend([tchar * tadd])
            if sval < 0:
                sadd = min(2, -sval) if sval < tval else min(1, -sval)
                sval += sadd
                if schar == ans[-1][0] and len(ans[-1]) + sadd >= 3:
                    break
                ans.extend([schar * sadd])
            if tval < 0:
                heapq.heappush(count, [tval, tchar])
            if sval and sval < 0:
                heapq.heappush(count, [sval, schar])
        return ''.join(ans[1:])

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
    flds = temp.replace("[","").replace("]","").replace(", ",",").rstrip().split(",")

    a, b, c = int(flds[0]), int(flds[1]), int(flds[2])
    print("a = {0:d}, b = {1:d}, c = {2:d}".format(a, b, c))

    sl = Solution()

    time0 = time.time()

    result = sl.longestDiverseString(a, b, c)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
