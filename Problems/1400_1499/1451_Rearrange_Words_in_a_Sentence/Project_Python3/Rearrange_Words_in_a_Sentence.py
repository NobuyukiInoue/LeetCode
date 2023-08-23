import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def arrangeWords(self, text: str) -> str:
        # 46ms - 48ms
        x = sorted(text.lower().split(" "), key = lambda s: len(s))
        return ' '.join([x[0].capitalize()] + x[1:])

    def arrangeWords_bad(self, text: str) -> str:
        # Time Limit Exceeded. 72/74
        words = text.split(" ")
        lengs = []
        for _, word in enumerate(words):
            lengs.append((len(word), word.lower()))
        n = len(lengs)
        for i in range(n - 1):
            for j in range(1, n):
                if lengs[j - 1][0] > lengs[j][0]:
                    lengs[j - 1], lengs[j] = lengs[j], lengs[j - 1]
        ans = lengs[0][1].capitalize()
        for i in range(1, len(lengs)):
            ans += " " + lengs[i][1]
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
    text = temp.replace("\"", "").replace("[", "").replace("]", "").rstrip()
    print("text = \"{0}\"".format(text))

    sl = Solution()
    time0 = time.time()

    result = sl.arrangeWords(text)

    time1 = time.time()

    print("result = \"{0}\"".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
