import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        # 95ms - 99ms
        lo, hi = 0, 1
        while lo < hi:
            mid = (lo + hi) / 2
            count, best = 0, [0, 1]
            left = 0
            for right in range(1, len(arr)):
                while arr[left] < mid * arr[right]:
                    left += 1
                count += left
                if left > 0 and best[0] * arr[right] < best[1] * arr[left - 1]:
                    best = [arr[left - 1], arr[right]]
            if count == k:
                return best
            elif count > k:
                hi = mid
            else:
                lo = mid
        return []

    def kthSmallestPrimeFraction2(self, arr: List[int], k: int) -> List[int]:
        # 1083ms - 1143ms
        len_arr, data = len(arr), []
        for i in range(0, len_arr - 1):
            for j in range(i + 1, len_arr):
                data.append((arr[i], arr[j], arr[i] / arr[j]))
        data.sort(key=lambda x: x[2])
        return [data[k - 1][0], data[k - 1][1]]
    
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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")

    arr = [int(n) for n in flds[0].split(",")]
    k = int(flds[1])
    print("arr = {0}, k = {1:d}".format(arr, k))

    sl = Solution()
    time0 = time.time()

    result = sl.kthSmallestPrimeFraction(arr, k)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
