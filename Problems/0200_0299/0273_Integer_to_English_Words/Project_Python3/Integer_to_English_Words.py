import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def numberToWords(self, num: int) -> str:
        # 36ms - 39ms
        ones = ['', ' One', ' Two', ' Three', ' Four', ' Five', ' Six', ' Seven', ' Eight', ' Nine', ' Ten', ' Eleven', ' Twelve', ' Thirteen', ' Fourteen', ' Fifteen', ' Sixteen', ' Seventeen', ' Eighteen', ' Nineteen']
        tens = ['', ' Ten', ' Twenty', ' Thirty', ' Forty', ' Fifty', ' Sixty', ' Seventy', ' Eighty', ' Ninety']
        thousands = ['', ' Thousand', ' Million', ' Billion']

        def helper(n: int) -> str:
            if n < 20:
                return ones[n]
            elif n < 100:
                return tens[n // 10] + helper(n % 10)
            elif n < 1000:
                return helper(n // 100) + ' Hundred' + helper(n % 100)
            else:
                for i in range(3, 0, -1):
                    if n >= 1000 ** i:
                        return helper(n // (1000 ** i)) + thousands[i] + helper(n % (1000 ** i))
            return ''

        if num == 0:
            return 'Zero'
        return helper(num).lstrip()

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
    num = int(fld)
    print("num = {0:d}".format(num))

    sl = Solution()
    time0 = time.time()

    result = sl.numberToWords(num)

    time1 = time.time()

    print("result = \"{0}\"".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
