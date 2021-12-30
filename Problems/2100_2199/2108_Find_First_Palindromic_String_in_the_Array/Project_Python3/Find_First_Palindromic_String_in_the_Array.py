import os
import re
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        # 60ms
        for word in words:
            if word == word[::-1]:
                return word
        return ""

    def firstPalindrome2(self, words: List[str]) -> str:
        # 68ms
        return next((w for w in words if w == w[::-1]), "")

    def firstPalindrome3(self, words: List[str]) -> str:
        # 104ms
        for word in words:
            isPalindrome = True
            lenWord = len(word)
            for i in range(lenWord//2):
                if word[i] != word[lenWord - 1 - i]:
                    isPalindrome = False
                    break
            if isPalindrome:
                return word
        return ""

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
    words = temp.replace("\"","").replace("[","").replace("]","").rstrip().split(",")
    print("words = {0}".format(words))

    sl = Solution()
    time0 = time.time()

    result = sl.firstPalindrome(words)

    time1 = time.time()

    print("result = \"{0}\"".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
