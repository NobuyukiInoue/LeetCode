import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def isBalanced(self, num: str) -> bool:
        # 0ms
        even, odd = 0, 0
        for i, ch in enumerate(num):
            if i % 2 == 0:
                even += int(ch)
            else:
                odd += int(ch)
        return even == odd

    def isBalanced2(self, num: str) -> bool:
        # 1ms - 3ms
        v_sum, sign = 0, 1
        for _i, ch in enumerate(num):
            v_sum += sign*int(ch)
            sign *= -1
        return v_sum == 0

    def isBalanced3(self, num: str) -> bool:
        # 0ms
        arr_num = list(map(int, num))
        return sum(arr_num[::2]) == sum(arr_num[1::2])

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
    num = temp.replace("\"", "").replace("[", "").replace("]", "").rstrip()
    print("num = \"{0}\"".format(num))

    sl = Solution()
    time0 = time.time()

    result = sl.isBalanced(num)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
