import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # 16ms
        pos = word.find(ch)
        return word[pos] + ''.join(list(reversed(word[:pos]))) + word[pos+1:] if pos >= 0 else word

    def reversePrefix2(self, word: str, ch: str) -> str:
        # 32ms
        return word[:word.find(ch)+1][::-1] + word[word.find(ch)+1:]


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
    word, ch = flds[0], flds[1]
    print("word = \"{0}\", ch = {1}".format(word, ch))

    sl = Solution()
    time0 = time.time()

    result = sl.reversePrefix(word, ch)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
