import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        # 24ms - 39ms
        res, stack = [], []
        for i, ch in enumerate(pattern + 'I', 1):
            stack.append(str(i))
            if ch == 'I':
                res += stack[::-1]
                stack = []
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
    pattern = temp.replace("\"", "").replace("[", "").replace("]", "").rstrip()
    print("pattern = {0}".format(pattern))

    sl = Solution()
    time0 = time.time()

    result = sl.smallestNumber(pattern)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
