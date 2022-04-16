import heapq
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def largestInteger(self, num: int) -> int:
        # 24ms - 42ms
        len_num = len(str(num))
        arr = [int(n) for n in str(num)]
        odd, even = [], []
        for n in arr:
            if n & 1:
                odd.append(n)
            else:
                even.append(n)
        odd.sort()
        even.sort()
        res = 0
        for i in range(len_num):
            if arr[i] & 1:
                res = res*10 + odd.pop()
            else:
                res = res*10 + even.pop()
        return res

    def largestInteger_heapq(self, num: int) -> int:
        # 31ms - 49ms
        len_num = len(str(num))
        arr = [int(n) for n in str(num)]
        odd, even = [], []
        for n in arr:
            if n & 1:
                heapq.heappush(odd, n)
            else:
                heapq.heappush(even, n)
        res, col = 0,  1
        for i in range(len_num - 1, -1, -1):
            if arr[i] & 1:
                res += heapq.heappop(odd)*col
            else:
                res += heapq.heappop(even)*col
            col *= 10
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
    flds = temp.replace("\"", "").replace("[", "").replace("]", "").rstrip()
    num = int(flds)
    print("num = {0:d}".format(num))

    sl = Solution()
    time0 = time.time()

    result = sl.largestInteger(num)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
