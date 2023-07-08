import bisect
import itertools
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # 796ms - 805ms
        ans = 0
        costs.sort()
        for _, cost in enumerate(costs):
            if coins < cost:
                break
            ans += 1
            coins -= cost
        return ans

    def maxIceCream_1liner(self, costs: List[int], coins: int) -> int:
        # 792ms - 813ms
        return bisect.bisect_right(list(itertools.accumulate(sorted(costs))), coins)
    
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

    costs = [int(n) for n in flds[0].split(",")]
    coins = int(flds[1])
    print("costs = {0}, coins = {1:d}".format(costs, coins))

    sl = Solution()
    time0 = time.time()

    result = sl.maxIceCream(costs, coins)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
