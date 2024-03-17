import heapq
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        # 35ms - 48ms
        t_cap, i = sum(apple), 0
        capacity = list(map(lambda x: -x, capacity))
        heapq.heapify(capacity)
        while t_cap > 0:
            t_cap += heapq.heappop(capacity)
            i += 1
        return i

    def minimumBoxes2(self, apple: List[int], capacity: List[int]) -> int:
        # 37ms - 47ms
        capacity.sort(reverse=True)
        total, t_cap = sum(apple), 0
        for i, cap in enumerate(capacity):
            if t_cap >= total:
                return i
            t_cap += cap
        return len(capacity)

    def minimumBoxes3(self, apple: List[int], capacity: List[int]) -> int:
        # 42ms - 49ms
        capacity.sort(reverse=True)
        total = sum(apple)
        t_cap, i = 0, 0
        while t_cap < total:
            t_cap += capacity[i]
            i += 1
        return i

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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    
    apple = [int(num) for num in flds[0].split(",")]
    capacity = [int(num) for num in flds[1].split(",")]
    print("apple = {0}, capacity = {1}".format(apple, capacity))

    sl = Solution()
    time0 = time.time()

    result = sl.minimumBoxes(apple, capacity)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
