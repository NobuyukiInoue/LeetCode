import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        # 28ms
        return sum(not set(word) & set(brokenLetters) for word in text.split())

    def canBeTypedWords2(self, text: str, brokenLetters: str) -> int:
        # 32ms
        ans = 0
        words = text.split()
        for word in words:
            used = False
            for ch in brokenLetters:
                if ch in word:
                    used = True
                    break
            if not used:
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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    text, brokenLetters = flds[0], flds[1]
    print("text = \"{0}\", brokenLetters = {1}".format(text, brokenLetters))

    sl = Solution()
    time0 = time.time()

    result = sl.canBeTypedWords(text, brokenLetters)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
