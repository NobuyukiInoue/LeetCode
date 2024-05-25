import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def numberOfSpecialChars_1liner(self, word: str) -> int:
        # 30ms - 36ms
        return len({ch for ch in word if ch.islower() and ch.upper() in word})

    def numberOfSpecialChars(self, word: str) -> int:
        # 30ms - 37ms
        lower = upper = 0
        for ch in word:
            if ch.islower():
                lower |= 1 << ord(ch) - 0x61
            else:
                upper |= 1 << ord(ch) - 0x41
        return (lower&upper).bit_count()

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

    result = sl.numberOfSpecialChars(word)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
