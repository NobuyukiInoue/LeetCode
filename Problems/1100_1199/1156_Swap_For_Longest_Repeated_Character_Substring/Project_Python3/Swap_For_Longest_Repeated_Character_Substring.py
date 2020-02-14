# coding: utf-8

import collections
import itertools
import os
import sys
import time

class Solution:
    #def maxRepOpt1(self, text: str) -> int:
    def maxRepOpt1(self, text):
        # 56ms
        A = [[c, len(list(g))] for c, g in itertools.groupby(text)]
        count = collections.Counter(text)
        res = max(min(k + 1, count[c]) for c, k in A)
        for i in range(1, len(A) - 1):
            if A[i - 1][0] == A[i + 1][0] and A[i][1] == 1:
                res = max(res, min(A[i - 1][1] + A[i + 1][1] + 1, count[A[i + 1][0]]))
        return res

def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
        print("Usage: python %s <testdata.txt>" %(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("%s not found..." %argv[1])
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        temp = temp.strip()
        if temp == "":
            continue
        print("args = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    text = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()
    print("text = {0}".format(text))
    time0 = time.time()

    sl = Solution()
    result = sl.maxRepOpt1(text)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
