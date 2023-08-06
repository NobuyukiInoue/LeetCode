# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        # 91ms
        return [w for word in words for w in word.split(separator) if w]

    def splitWordsBySeparator2(self, words: List[str], separator: str) -> List[str]:
        # 97ms
        ans = []
        for word in words:
            flds = word.split(separator)
            for fld in flds:
                if fld != "":
                    ans.append(fld)
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
    flds = temp.replace(", ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    words = flds[0].split(",")
    separator = flds[1]
    print("words = \"{0}\", separator = {1}".format(words, separator))

    sl = Solution()
    time0 = time.time()

    result = sl.splitWordsBySeparator(words, separator)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
