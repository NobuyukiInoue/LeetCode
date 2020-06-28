# coding: utf-8

import os
import sys
import time
from collections import Counter as cnt

class Solution:
#   def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    def longestCommonSubsequence(self, text1, text2):
        # 448ms
        len1, len2 = len(text1), len(text2)
        matrix = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]

        for i in range(len1):
            for j in range(len2):
                if text1[i] == text2[j]:
                    matrix[i + 1][j + 1] = matrix[i][j] + 1
                else:
                    matrix[i + 1][j + 1] = max(matrix[i + 1][j], matrix[i][j + 1])

        return matrix[len1][len2]

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

    text1, text2 = flds[0], flds[1]
    print("text1 = = {0}, text2 = {1}".format(text1, text2))

    sl = Solution()

    time0 = time.time()

    result = sl.longestCommonSubsequence(text1, text2)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
