import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def minRemoveToMakeres(self, s: str) -> str:
        # 118ms - 244ms 
        res, stack, brackets = list(s), [], '()'
        for i, ch in enumerate(s):
            if ch not in brackets:
                continue
            if ch == '(':
                stack.append(i)
            else:
                if not stack:
                    res[i] = ''
                else:
                    stack.pop()
        while stack:
            res[stack.pop()] = ''
        return ''.join(res)

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
    print("word = \"{0}\"".format(s))

    sl = Solution()
    time0 = time.time()

    result = sl.minRemoveToMakeres(s)

    time1 = time.time()

    print("result = \"{0}\"".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
