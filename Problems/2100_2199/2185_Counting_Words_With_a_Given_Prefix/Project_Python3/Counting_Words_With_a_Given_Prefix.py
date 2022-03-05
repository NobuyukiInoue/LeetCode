# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        # 40ms
        ans = 0
        for word in words:
            if word.startswith(pref):
                ans += 1
        return ans

    def prefixCount_use_find(self, words: List[str], pref: str) -> int:
        # 53ms
        ans = 0
        for word in words:
          # if word.find(pref) == 0:
            if word.startswith(pref):
                ans += 1
        return ans

    def prefixCount_use_array(self, words: List[str], pref: str) -> int:
        # 51ms
        ans, len_pref = 0, len(pref)
        for word in words:
            if word[0:len_pref] == pref:
                ans += 1
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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    words = flds[0].split(",")
    pref = flds[1]
    print("words = {0}, pref = {1}".format(words, pref))

    sl = Solution()
    time0 = time.time()

    result = sl.prefixCount(words, pref)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
