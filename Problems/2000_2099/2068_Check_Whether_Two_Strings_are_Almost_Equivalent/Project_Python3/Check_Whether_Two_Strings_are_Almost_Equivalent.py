import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        # 20ms
        cnt1, cnt2 = collections.Counter(word1), collections.Counter(word2)
        for k in cnt1.keys():
            if abs(cnt1[k] - cnt2[k]) > 3:
                return False
        for k in cnt2.keys():
            if abs(cnt1[k] - cnt2[k]) > 3:
                return False
        return True

    def checkAlmostEquivalent2(self, word1: str, word2: str) -> bool:
        # 24ms
        return all(v < 4 for v in ((collections.Counter(word1) - collections.Counter(word2)) + (collections.Counter(word2) - collections.Counter(word1))).values())

    def checkAlmostEquivalent3(self, word1: str, word2: str) -> bool:
        # 36ms
        f1, f2 = [0] * 26, [0] * 26
        for ch in word1:
            f1[ord(ch) - ord('a')] += 1
        for ch in word2:
            f2[ord(ch) - ord('a')] += 1
        for i in range(26):
            if abs(f1[i] - f2[i]) > 3:
                return False
        return 

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
    flds = temp.replace("\"", "").replace("[[", "").replace("]]", "").rstrip().split("],[")
    word1, word2 = flds[0], flds[1]
    print("word1 = \"{0}\", word2 = {1}".format(word1, word2))

    sl = Solution()
    time0 = time.time()

    result = sl.checkAlmostEquivalent(word1, word2)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
