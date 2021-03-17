import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # 24ms
        minLen = min(len(word1), len(word2))
        res = ""
        for i in range(minLen):
            res += word1[i] + word2[i]
        res += word1[minLen:] + word2[minLen:]
        return res

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
    flds = temp.replace(", ",",").replace("\"","").replace("[","").replace("]","").rstrip().split(",")

    word1, word2 = flds[0], flds[1]
    print("word1 = {0}, word2 = {1}".format(word1, word2))

    sl = Solution()
    time0 = time.time()

    result = sl.mergeAlternately(word1, word2)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
