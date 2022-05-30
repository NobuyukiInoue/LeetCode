import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def digitCount(self, num: str) -> bool:
        # 35ms - 53ms
        cnts = collections.Counter(num)
        for i, _ in enumerate(num):
            if cnts[str(i)] != int(num[i]):
                return False
        return True

    def digitCount_2liner(self, num: str) -> bool:
        # 43ms - 75ms
        cnts = collections.Counter(map(int, num))
        return all(cnts[i] == int(n) for i, n in enumerate(num))

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
    num = temp.replace("\"", "").replace("[", "").replace("]", "").rstrip()
    print("num = {0}".format(num))

    sl = Solution()
    time0 = time.time()

    result = sl.digitCount(num)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
