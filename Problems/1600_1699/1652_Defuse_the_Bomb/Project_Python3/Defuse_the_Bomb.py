# coding: utf-8

import os
import sys
import time
import math

class Solution:
#   def decrypt(self, code: List[int], k: int) -> List[int]:
    def decrypt(self, code: [int], k: int) -> [int]:
        # 32ms
        if k < 0:
            return self.decrypt(code[::-1], -k)[::-1]
        n = len(code)
        prefix = code*2
        for i in range(1, 2*n):
            prefix[i] += prefix[i - 1]
        for i in range(n):
            code[i] = prefix[i + k] - prefix[i]
        return code

    def decrypt2(self, code: [int], k: int) -> [int]:
        # 40ms
        if k < 0:
            return self.decrypt(code[::-1], -k)[::-1]
        n = len(code)
        prefix = code * 2
        for i in range(2 * n):
            prefix[i] += i > 0 and prefix[i - 1]
            if k <= i < n + k:
                code[i - k] = prefix[i] - prefix[i - k]
        return code

    def decrypt3(self, code: [int], k: int) -> [int]:
        # 48ms
        codeLen = len(code)
        res = [0]*len(code)
        if k > 0:
            for i, _ in enumerate(code):
                for nextk in range(i + 1, i + 1 + k):
                    if nextk >= codeLen:
                        nextk -= codeLen
                    res[i] += code[nextk]
        elif k < 0:
            for i, _ in enumerate(code):
                for prevk in range(i - 1, i - 1 + k, -1):
                    if prevk < 0:
                        prevk += codeLen
                    res[i] += code[prevk]
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
    flds = temp.replace("[[","").replace("]]","").replace("\"","").replace(" ","").rstrip().split("],[")
    code = [int(n) for n in flds[0].split(",")]
    k = int(flds[1])
    print("code = {0}, k = {1:d}".format(code, k))

    sl = Solution()

    time0 = time.time()

    result = sl.decrypt(code, k)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
