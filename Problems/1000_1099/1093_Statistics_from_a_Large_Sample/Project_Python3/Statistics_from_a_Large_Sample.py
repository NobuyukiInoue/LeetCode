import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        # 40ms - 50ms
        v_min = v_max = -1
        n = v_sum = 0
        v_maxcnt = mode = 0
        for i, cur in enumerate(count):
            if cur == 0:
                continue
            if v_min == -1:
                v_min = i
            v_max = max(v_max, i)
            n += cur
            v_sum += i*cur
            if cur > v_maxcnt:
                v_maxcnt = cur
                mode = i

        def kth(k):
            for i, cur in enumerate(count):
                k -= cur
                if k <= 0:
                    return i

        if n%2 == 1:
            median = kth(n//2 + 1)
        else:
            median = (kth(n//2) + kth(n//2 + 1))/2
        return [v_min, v_max, v_sum/n, median, mode]

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
    count = [int(n) for n in flds.split(",")]
    print("count = {0}".format(count))

    sl = Solution()

    time0 = time.time()

    result = sl.sampleStats(count)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
