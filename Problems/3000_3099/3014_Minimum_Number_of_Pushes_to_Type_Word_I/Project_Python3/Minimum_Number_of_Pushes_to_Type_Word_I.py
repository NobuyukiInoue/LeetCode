import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def minimumPushes(self, word: str) -> int:
        # 37ms - 38ms
        n, row, ans = len(word), 1, 0
        for _ in range(n//8, 0, -1):
            ans += row*8
            row += 1
        return ans + (n%8)*row

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

    result = sl.minimumPushes(word)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
