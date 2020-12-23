import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def numSteps(self, s: str) -> int:
        # 32ms
        res, carry = 0, 0
        for i in range(len(s) - 1, 0, -1):
            res += 1
            if ord(s[i]) - ord("0") + carry == 1:
                carry = 1
                res += 1
        return res + carry

    def numSteps3(self, s: str) -> int:
        # 32ms
        n = int(s, 2)
        res = 0
        while n > 1:
            if n % 2 == 1:
                n += 1
            else:
                n //= 2
            res += 1
        return res

    def numStep2(self, s: str) -> int:
        # 24ms
        s = list(s)
        index, carry, steps = len(s) - 1, False, 0
        prev_index_with_one = len(s) - 1
        while index > 0:
            if carry:
                if s[index] == '0':
                    steps += prev_index_with_one - index
                    s[index] = '1'
                    index += 1
                    carry = False
            else:
                if s[index] == '0':
                    steps += 1
                else:
                    prev_index_with_one = index
                    steps += 1
                    carry = True
            index -= 1
        if carry:
            steps += prev_index_with_one + 1
        return steps

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
    s = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    print("s = {0}".format(s))

    sl = Solution()
    time0 = time.time()

    result = sl.numSteps(s)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
