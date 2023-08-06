import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # 29ms - 36ms
        d = (purchaseAmount + 5)//10
        return 100 - d*10

    def accountBalanceAfterPurchase_1liner(self, purchaseAmount: int) -> int:
        # 45ms - 46ms
        return 100 - ((purchaseAmount + 5)//10)*10

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
    fld = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    purchaseAmount = int(fld)
    print("purchaseAmount = {0:d}".format(purchaseAmount))

    sl = Solution()
    time0 = time.time()

    result = sl.accountBalanceAfterPurchase(purchaseAmount)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
