import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        # 32ms - 37ms
        smDigits, temp_x = 0, x
        while temp_x > 0:
            smDigits += temp_x%10
            temp_x //= 10
        return smDigits if x%smDigits == 0 else -1

    def sumOfTheDigitsOfHarshadNumber_2liner(self, x: int) -> int:
        # 33ms - 40ms
        smDigits = sum(map(int, str(x)))
        return smDigits if x % smDigits == 0 else -1

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
    flds = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    
    x = int(flds)
    print("x = {0:d}".format(x))

    sl = Solution()
    time0 = time.time()

    result = sl.sumOfTheDigitsOfHarshadNumber(x)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
