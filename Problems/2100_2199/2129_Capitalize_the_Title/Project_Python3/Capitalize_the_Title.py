import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        # 32ms
        res = ""
        for word in title.split(" "):
            if len(word) < 3:
                res += " " + word.lower()
            else:
                word = word.lower()
                res += " " + word[0].upper() + word[1:]
        return res[1:]

    def capitalizeTitle_oneLiner(self, title: str) -> str:
        # 48ms
        return " ".join(w.lower() if len(w) <= 2 else w[0].upper() + w[1:].lower() for w in title.split())

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
    title = temp.replace("\"", "").replace("[", "").replace("]", "").rstrip()
    print("title = \"{0}\"".format(title))

    sl = Solution()
    time0 = time.time()

    result = sl.capitalizeTitle(title)

    time1 = time.time()

    print("result = \"{0}\"".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
