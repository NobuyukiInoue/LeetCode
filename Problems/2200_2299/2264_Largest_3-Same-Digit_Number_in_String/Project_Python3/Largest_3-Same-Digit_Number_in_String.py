import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # 32ms - 86ms
        res, cnt = '', 1 
        for i in range(1, len(num)):
            if num[i] == num[i-1]:
                cnt += 1
            else:
                cnt = 1
            if cnt == 3:
                res = max(res, num[i] * 3)
        return res

    def largestGoodInteger_OneLiner(self, num: str) -> str:
        # 40ms - 70ms
        return max((num[i:i+3] for i in range(len(num)-2) if num[i] == num[i+1] == num[i+2]), default="")

    def largestGoodInteger_intMax(self, num: str) -> str:
        # 643ms - 783ms
        ans, isNone = 0, True
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                isNone = False
                ch = num[i]
                ans = max(ans, int(num[i:i+3]))
                if i < len(num) - 3:
                    i += 3
                while num[i] == ch and i < len(num) - 1:
                    i += 1
        if isNone:
            return ""
        return str("{0:03d}".format(ans))

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

    result = sl.largestGoodInteger(num)

    time1 = time.time()

    print("result = \"{0}\"".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
