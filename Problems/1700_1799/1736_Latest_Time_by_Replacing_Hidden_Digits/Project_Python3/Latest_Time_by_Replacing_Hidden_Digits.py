import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def maximumTime(self, time: str) -> str:
        # 32ms
        res = ""

        if time[0] == '?':
            if time[1] in "0123?":
                res = '2'
            else:
                res = '1'
        else:
            res = time[0]

        if time[1] == '?':
            if res[0] == '2':
                res += '3'
            else:
                res += '9'
        else:
            res += time[1]

        res += ":"

        if time[3] == '?':
            res += '5'
        else:
            res += time[3]

        if time[4] == '?':
            res += '9'
        else:
            res += time[4]

        return res

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
    vartime = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    print("time = {0}".format(vartime))

    sl = Solution()
    time0 = time.time()

    result = sl.maximumTime(vartime)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
