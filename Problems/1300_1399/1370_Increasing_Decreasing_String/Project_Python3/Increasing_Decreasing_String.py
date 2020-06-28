# coding: utf-8

import collections
import os
import re
import sys
import time

class Solution:
#   def sortString(self, s: str) -> str:
    def sortString(self, s):
        # 56ms
        cnt, ans, asc = collections.Counter(s), [], True
        while cnt:
            for c in sorted(cnt.keys()) if asc else reversed(sorted(cnt.keys())):
                ans.append(c)
                cnt[c] -= 1
                if cnt[c] == 0:
                    del cnt[c]
            asc = not asc
        return ''.join(ans)

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
    s = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()

    sl = Solution()
    time0 = time.time()

    result = sl.sortString(s)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
