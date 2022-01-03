import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        # 79ms
        if '0' not in binary:
            return binary
        k, n = binary.count('1', binary.find('0')), len(binary)
        return '1' * (n - k - 1) + '0' + '1' * k

    def maximumBinaryString_easy(self, binary: str) -> str:
        # 450ms
        c = 0
        lst = ["1"]*len(binary)
        for i, _ in enumerate(binary):
            if binary[i] == "0":
                c += 1
        for i, _ in enumerate(binary):
            if binary[i] == "0":
                lst[i + c - 1] = "0"
                return "".join(lst)
        return binary

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
    binary = temp.replace("\"", "").replace("[", "").replace("]", "").rstrip()
    print("binary = \"{0}\"".format(binary))

    sl = Solution()
    time0 = time.time()

    result = sl.maximumBinaryString(binary)

    time1 = time.time()

    print("result = \"{0}\"".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
