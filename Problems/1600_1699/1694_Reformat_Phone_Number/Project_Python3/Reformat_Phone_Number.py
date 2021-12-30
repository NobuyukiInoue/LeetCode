import os
import re
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def reformatNumber2(self, number: str) -> str:
        # 28ms
        return re.sub('(...?(?=..))', r'\1-', re.sub('\D', '', number))

    def reformatNumber(self, number: str) -> str:
        # 28ms
        number = ''.join(number.split('-'))
        number = ''.join(number.split())
        if len(number) <= 3:
            return number
        if len(number) == 4:
            return number[:2] + '-' + number[2:]
        i = 0
        s = ''
        while i < len(number):
            s += number[i:i+3] + '-'
            i += 3
            if len(number) - i <= 4:
                if len(number)- i == 4:
                    return s + number[i:(i + 2)] + '-' + number[(i + 2):]
                return s + number[i:]
        return s[:-1]
        
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
    number = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    print("number = {0}".format(number))

    sl = Solution()
    time0 = time.time()

    result = sl.reformatNumber(number)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
