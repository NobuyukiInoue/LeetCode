import heapq
import math
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # 44ms - 50ms
        gifts = [-num for num in gifts]
      # gifts = list(map(lambda x: x*(-1), gifts))
        heapq.heapify(gifts)
        for i in range(k):
            m = heapq.heappop(gifts)*(-1)
            heapq.heappush(gifts, -math.isqrt(m))
        return -sum(gifts)

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

    gifts = [int(n) for n in flds[0].split(",")]
    k = int(flds[1])
    print("gifts = {0}, k = {1:d}".format(gifts, k))

    sl = Solution()
    time0 = time.time()

    result = sl.pickGifts(gifts, k)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
