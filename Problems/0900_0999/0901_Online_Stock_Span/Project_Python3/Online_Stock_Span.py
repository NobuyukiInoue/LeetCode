import os
import sys
import time
from typing import List, Dict, Tuple

class StockSpanner:
    # 436ms
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        self.stack.append([price, res])
        return res


class StockSpanner2:
    # Time Limit Exceeded.
    def __init__(self):
        self.nums = []

    def next(self, price: int) -> int:
        i = len(self.nums) - 1
        res = 1
        while i >= 0 and self.nums[i] <= price:
            res += 1
            i -= 1
        self.nums.append(price)
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner(big, medium, small)
# param_1 = obj.addCar(carType)

class Solution:
    def main(self, cmds, args):
        res = []
        for i in range(len(cmds)):
            if cmds[i] == "StockSpanner":
                stockSpanner = StockSpanner()
                res.append(None)
                print("Exec StockSpanner().")
            else:
                if StockSpanner is None:
                    print("StockSpanner not found... {0}".format(cmds[i]))
                    exit(1)
                elif cmds[i] == "next":
                    res.append(stockSpanner.next(args[i]))
                    print("next({0}) ... {1}".format(args[i], res[-1]))
                else:
                    print("error... {0}".format(cmds[i]))
                    exit(1)
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
    flds = temp.replace("\"","").replace(", ",",").rstrip().split("],[[")
    cmds = flds[0].replace("[", "").replace("]", "").split(",")
    args = flds[1].replace("]]]","").split("],[")
#   args[0] = [int(_) for _ in args[0].split(",")]
    for i in range(1, len(args)):
        args[i] = int(args[i])

    print("cmds[] = {0}".format(cmds))
    print("args[] = {0}".format(args))

    sl = Solution()
    time0 = time.time()
    result = sl.main(cmds, args)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
