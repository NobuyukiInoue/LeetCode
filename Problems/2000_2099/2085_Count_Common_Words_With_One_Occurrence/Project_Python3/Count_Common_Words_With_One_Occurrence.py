import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        # 64ms
        dic1 = collections.Counter(words1)
        dic2 = collections.Counter(words2)
        return sum(1 for k in dic1.keys() if dic1[k] == dic2[k] == 1)

    def countWords2(self, words1: List[str], words2: List[str]) -> int:
        # 64ms
        dic1 = collections.Counter(words1)
        dic2 = collections.Counter(words2)
        ans = 0
        for k in dic1.keys():
            if dic1[k] == dic2[k] == 1:
                ans += 1
        return ans

    def countWords_oneliner(self, words1: List[str], words2: List[str]) -> int:
        # 68ms
        return len(set(k for k, v in collections.Counter(words1).items() if v == 1) & set(k for k, v in collections.Counter(words2).items() if v == 1))

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
    word1, word2 = flds[0].split(","), flds[1].split(",")
    print("word1 = \"{0}\", word2 = {1}".format(word1, word2))

    sl = Solution()
    time0 = time.time()

    result = sl.countWords(word1, word2)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
