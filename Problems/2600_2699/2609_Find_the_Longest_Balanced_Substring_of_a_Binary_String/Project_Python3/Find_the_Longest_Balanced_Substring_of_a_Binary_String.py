import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def findTheLongestBalancedSubstring1(self, s: str) -> int:
        # 39ms - 40ms
        temp, res = "01", 0
        while len(temp) <= len(s):
            if temp in s:
                res = len(temp)
            temp = "0" + temp + "1"
        return res

    def findTheLongestBalancedSubstring(self, s: str) -> int:
        # 37ms - 50ms
        res, i = 0, 0
        while i < len(s):
            z, o = 0, 0
            while i < len(s) and s[i] == '0':
                z += 1
                i += 1
            while i < len(s) and s[i] =='1' and z > o:
                o += 1
                i += 1
                res = max(res, o*2)
            while i < len(s) and s[i] == '1':
                i += 1
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
    s = temp.replace("\"", "").replace("[", "").replace("]", "").rstrip()
    print("s = {0}".format(s))

    sl = Solution()
    time0 = time.time()

    result = sl.findTheLongestBalancedSubstring(s)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
