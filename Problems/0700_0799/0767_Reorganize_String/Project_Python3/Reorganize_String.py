import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def reorganizeString(self, s: str) -> str:
        # 20ms
        count = collections.Counter(s)
        c_max, f_max = count.most_common(1)[0]
        if 2 * f_max - 1 > len(s):
            return ""
        count.pop(c_max)
        res = len(s) * [""]
        res[:2*f_max:2] = f_max * [c_max]
        i = 2 * f_max
        for c in count:
            for _ in range(count[c]):
                if i >= len(s):
                    i = 1
                res[i] = c
                i += 2
        return "".join(res)

    def reorganizeString2(self, s: str) -> str:
        # 28ms
        a = sorted(sorted(s), key=s.count)
        h = len(a) // 2
        a[1::2], a[::2] = a[:h], a[h:]
        return ''.join(a) * (a[-1:] != a[-2:-1])

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

    result = sl.reorganizeString(s)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
