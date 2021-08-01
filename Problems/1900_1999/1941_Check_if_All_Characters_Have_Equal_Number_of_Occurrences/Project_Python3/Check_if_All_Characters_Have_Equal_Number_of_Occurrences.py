import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        # 28ms
        return len(set(collections.Counter(s).values())) == 1
        
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
    s = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    print("s = {0}".format(s))

    sl = Solution()
    time0 = time.time()

    result = sl.areOccurrencesEqual(s)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
