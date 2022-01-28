import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        # 28ms
        res = [s[i : i + k] for i in range(0, len(s), k)]
        if len(res[-1]) != k : res[-1] = res[-1] + fill*(k - len(res[-1]))
        return res

    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        # 32ms
        res = []
        if len(s)%k == 0:
            for i in range(0, len(s), k):
                res.append(s[i:i + k])
        else:
            temp = len(s)%k
            last = 0
            for i in range(0, len(s) - temp, k):
                res.append(s[i:i + k])
                last = i + k
            final = s[last:] + fill*(k - temp)
            res.append(final)
        return res

    def divideString3(self, s: str, k: int, fill: str) -> List[str]:
        # 55ms
        res = []
        i = 0
        while i + k <= len(s):
            res.append(s[i:i+k])
            i += k
        if i < len(s):
            fmt = "{0:" + str(k) + "s}"
            res.append(fmt.format(s[i:len(s)]).replace(" ", fill))
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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    s, k, fill = flds[0], int(flds[1]), flds[2]
    print("s = \"{0}\", k = {1:d}, fill = \"{2}\"".format(s, k, fill))

    sl = Solution()
    time0 = time.time()

    result = sl.divideString(s, k, fill)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
