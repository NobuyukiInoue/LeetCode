# coding: utf-8

import itertools
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        # 54ms - 68ms
        return [next(g) for _, g in itertools.groupby(words, sorted)]

    def removeAnagrams_1liner(self, words: List[str]) -> List[str]:
        # 58ms - 90ms
        return [words[i] for i in range(0, len(words)) if i == 0 or sorted(words[i]) != sorted(words[i - 1])]

    def removeAnagrams_work(self, words: List[str]) -> List[str]:
        # 62ms - 74ms
        ans = []
        ans.append(words[0])
        dif1 = sorted(words[0])
        for i in range(1, len(words)):
            dif2 = sorted(words[i])
            if dif1 != dif2:
                ans.append(words[i])
            dif1 = dif2
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
    flds = temp.replace(" ","").replace("\"","").replace("[","").replace("]","").rstrip()
    words = flds.split(",")
    print("words = {0}".format(words))
  
    sl = Solution()
    time0 = time.time()

    result = sl.removeAnagrams(words)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
