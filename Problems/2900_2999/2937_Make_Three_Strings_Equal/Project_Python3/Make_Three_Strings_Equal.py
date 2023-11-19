import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        # 50ms - 52ms
        min_length = min(len(s1), len(s2), len(s3))
        total_length = len(s1) + len(s2) + len(s3)
        if s1[0] != s2[0] or s1[0] != s3[0] or s2[0] != s3[0]:
            return -1
        for i in range(min_length):
            if s1[i] == s2[i] == s3[i]:
                total_length -= 3
            else:
                break
        return total_length

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
    flds = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").rstrip().split(",")
    s1, s2, s3 = flds[0], flds[1], flds[2]
    print("s1= {0}, s1 = {1}, s3 = {2}".format(s1, s2, s3))

    sl = Solution()
    time0 = time.time()

    result = sl.findMinimumOperations(s1, s2, s3)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
