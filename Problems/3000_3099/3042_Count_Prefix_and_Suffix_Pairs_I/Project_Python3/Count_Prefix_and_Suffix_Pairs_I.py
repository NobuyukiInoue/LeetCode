import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        # 49ms - 65ms
        ans = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    ans += 1
        return ans

    def countPrefixSuffixPairs2(self, words: List[str]) -> int:
        # 60ms - 63ms
        def isinSuffix(s1: str, s2: str) -> bool:
            if s2.startswith(s1) and s2.endswith(s1):
                return True
            return False
        ans = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if isinSuffix(words[i], words[j]):
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
    words = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").rstrip().split(",")
    print("words = {0}".format(words))

    sl = Solution()
    time0 = time.time()

    result = sl.countPrefixSuffixPairs(words)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
