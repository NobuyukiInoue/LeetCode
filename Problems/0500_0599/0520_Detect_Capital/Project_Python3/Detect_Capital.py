# coding: utf-8

import os
import sys
import time

class Solution:
#    def detectCapitalUse(self, word: str) -> bool:
    def detectCapitalUse(self, word):
        return word.isupper() or word.islower() or word.istitle()

    def detectCapitalUse2(self, word):
        return word == word.upper() or word == word.lower() or (
            word[0] == word[0].upper() and word[1:] == word[1:].lower())

    def detectCapitalUse_work(self, word):
        if ord(word[0]) >= ord("a") and ord(word[0]) <= ord("z"):
            for ch in word:
                if ord(ch) < ord("a") or ord(ch) > ord("z"):
                    return False
            return True
        elif ord(word[0]) >= ord("A") and ord(word[0]) <= ord("Z"):
            upper_count = 0
            for ch in word:
                if ord(ch) >= ord("A") and ord(ch) <= ord("Z"):
                    upper_count += 1
            if upper_count == len(word):
                return True
            elif upper_count == 1 and ord(word[0]) >= ord("A") and ord(word[0]) <= ord("Z"):
                return True
            return False
        return False

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
    word = temp.replace("\"","").replace(" ","").replace("[","").replace("]","").rstrip()
    print("word = {0}".format(word))

    sl = Solution()
    time0 = time.time()

    result = sl.detectCapitalUse(word)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
