import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 60ms
        len_s1 = len(s1)
        dic_s1 = collections.Counter(s1)
        dic_s2 = collections.Counter(s2[:len_s1])
        if dic_s1 == dic_s2:
            return True
        for i in range(len_s1, len(s2)):
            dic_s2[s2[i]] += 1

            if dic_s2[s2[i - len_s1]] > 1:
                dic_s2[s2[i - len_s1]] -= 1
            else:
                dic_s2.pop(s2[i - len_s1], None)
            if dic_s1 == dic_s2:
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
    flds = temp.replace(", ", ",").replace("\"","").replace("[","").replace("]","").rstrip().split(",")
    s1, s2 = flds[0], flds[1]

    print("s1 = {0}".format(s1))
    print("s2 = {0}".format(s2))

    sl = Solution()
    time0 = time.time()

    result = sl.checkInclusion(s1, s2)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
