import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        # 24ms
        ans = 0
        for i, _ in enumerate(patterns):
            if patterns[i] in word:
                ans += 1
        return ans

    def numOfStrings2(self, patterns: List[str], word: str) -> int:
        # 36ms
        return sum(map(lambda p: p in word, patterns))

    def numOfStrings_bad(self, patterns: List[str], word: str) -> int:
        targets = [k for k, _ in collections.Counter(word).items()]
        ans = 0
        for pattern in patterns:
            for ch in targets:
                if ch in pattern:
                    ans += 1
                    break
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
    flds = temp.replace("\"","").replace(", ",",").replace("[[","").replace("]]","").rstrip().split("],[")
    patterns, word = flds[0].split(","), flds[1]
    print("patterns = \"{0}\", word = {1}".format(patterns, word))

    sl = Solution()
    time0 = time.time()

    result = sl.numOfStrings(patterns, word)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
