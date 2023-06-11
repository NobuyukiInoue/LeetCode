import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # 72ms - 80ms
        prices.sort()
        if prices[0] + prices[1] <= money:
            return money - (prices[0] + prices[1])
        return money

    def buyChoco2(self, prices: List[int], money: int) -> int:
        # 77ms - 78ms
        first_min = second_min = sys.maxsize
        for p in prices:
            if p < first_min:
                second_min, first_min = first_min, p
            elif p < second_min:
                second_min = p
        min_price = first_min + second_min
        return money - min_price if min_price <= money else money
    
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

    prices = [int(n) for n in flds[0].split(",")]
    money = int(flds[1])
    print("prices = {0}, money = {1:d}".format(prices, money))

    sl = Solution()
    time0 = time.time()

    result = sl.buyChoco(prices, money)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
