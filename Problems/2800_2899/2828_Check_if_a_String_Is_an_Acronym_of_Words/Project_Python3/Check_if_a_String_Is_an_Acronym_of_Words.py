# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        # 47ms - 66ms
        target = ""
        for word in words:
            target += word[0]
        return target == s

    def isAcronym_1liner(self, words: List[str], s: str) -> bool:
        # 51ms - 68ms
        return ''.join(word[0] for word in words) == s


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
    flds = temp.replace(", ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    words = flds[0].split(",")
    s = flds[1]
    print("words = \"{0}\", s = {1}".format(words, s))

    sl = Solution()
    time0 = time.time()

    result = sl.isAcronym(words, s)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
