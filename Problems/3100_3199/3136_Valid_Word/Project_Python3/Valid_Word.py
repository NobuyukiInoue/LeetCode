import os
import re
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def isValid_2liner(self, word: str) -> bool:
        # 20ms - 34ms
        regex = r"(?i)(?=^.*[b-df-hj-np-tv-z])(?=.*[aieou])^[a-z0-9]{3,}$"
        return re.search(regex, word) is not None

    def isValid(self, word: str) -> bool:
        # 33ms - 39ms
        if len(word) < 3 or '@' in word or '#' in word or '$' in word:
            return False
        is_vowel, is_consonant = False, False
        word = word.lower()
        for ch in word:
            if ch in 'aeiou':
                is_vowel = True
            elif ord(ch) > 97 and ord(ch) < 123:
                is_consonant = True
            if is_consonant and is_vowel:
                return True
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
    word = temp.replace("\"", "").replace("[", "").replace("]", "").rstrip()
    print("word = \"{0}\"".format(word))

    sl = Solution()
    time0 = time.time()

    result = sl.isValid(word)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
