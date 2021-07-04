import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # 44ms
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)

    def longestSubstring2(self, s: str, k: int) -> int:
        # 32ms
        return self.check(s, k)

    def check(self, s, k):
        if len(s) == 0:
            return 0
        d = {}
        for l in s:
            try:
                d[l] += 1
            except:
                d[l] = 1
        stop = []
        for key in d.keys():
            if d[key] < k:
                stop.append(key)
        if len(stop) == 0:
            return len(s)
        valid_s = []
        start = 0
        for i in range(len(s)):
            if s[i] in stop:
                valid_s.append(s[start:i])
                start = i + 1
        valid_s.append(s[start:])
        max_v = 0
        for vs in valid_s:
            if len(vs) == 0:
                continue
            tmp = self.check(vs, k)
            if tmp > max_v:
                max_v = tmp
        return max_v

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
    s, k = flds[0], int(flds[1])
    print("s = \"{0}\", k = {1:d}".format(s, k))

    sl = Solution()
    time0 = time.time()

    result = sl.longestSubstring(s, k)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
