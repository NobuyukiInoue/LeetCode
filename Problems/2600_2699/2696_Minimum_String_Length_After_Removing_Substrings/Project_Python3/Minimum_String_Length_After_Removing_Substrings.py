import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def minLength(self, s: str) -> int:
        # 47ms
        stack = []
        for ch in s:
            if stack and stack[-1] + ch in ("AB", "CD"):
                stack.pop()
            else:
                stack.append(ch)
        return len(stack)

    def minLength2(self, s: str) -> int:
        # 64ms
        prev = len(s)+1
        while len(s) < prev:
            s, prev = s.replace("AB", "").replace("CD", ""), len(s)
        return prev

    def minLength3(self, s: str) -> int:
        # 63ms
        arr_s = list(s)
        i = 0
        while i < len(arr_s) - 1:
            if arr_s[i] == "A" and arr_s[i + 1] == "B":
                del arr_s[i : i + 2]
                i = max(0, i - 1)
            elif arr_s[i] == "C" and arr_s[i + 1] == "D":
                del arr_s[i : i + 2]
                i = max(0, i - 1)
            else:
                i += 1
        return len(arr_s)
       
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

    result = sl.minLength(s)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
