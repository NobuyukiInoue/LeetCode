import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def partitionString(self, s: str) -> int:
        # 137ms - 266ms
        ans = 1
        arr = set()
        for ch in s:
            if ch in arr:
                ans += 1
                arr = set()
            arr.add(ch)
        return ans

    def partitionString_xor(self, s: str) -> int:
        # 608ms - 668ms
        bit, ans = 0, 1
        for ch in s:
            shift = ord(ch) - ord('a')
            if bit&(1<<shift) != 0:
                ans += 1
                bit = 0
            bit ^= 1 << shift
        return ans

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

    result = sl.partitionString(s)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
