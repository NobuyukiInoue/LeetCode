import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # 345ms - 347ms
        best, clen = 0, 0
        for i in range(len(arr)):
            if i >= 2 and (arr[i-2] > arr[i-1] < arr[i] or arr[i-2] < arr[i-1] > arr[i]):
                clen += 1
            elif i >= 1 and arr[i-1] != arr[i]:
                clen = 2
            else:
                clen = 1
            best = max(best, clen)
        return best

    def maxTurbulenceSize2(self, arr: List[int]) -> int:
        # 317ms - 328m
        ans, n, l, r = 1, len(arr), 0, 0
        if n == 1:
            return 1
        while r < n:
            while l < n - 1 and arr[l] == arr[l+1]:
                l += 1
            while r < n - 1 and (arr[r-1] > arr[r] < arr[r+1] or arr[r-1] < arr[r] > arr[r+1]):
                r += 1
            ans = max(ans, r - l + 1)
            l = r
            r += 1
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
    flds = temp.replace("[","").replace("]","").replace(", ",",").rstrip()
    arr = [int(n) for n in flds.split(",")]
    print("arr = {0}".format(arr))

    sl = Solution()

    time0 = time.time()

    result = sl.maxTurbulenceSize(arr)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
