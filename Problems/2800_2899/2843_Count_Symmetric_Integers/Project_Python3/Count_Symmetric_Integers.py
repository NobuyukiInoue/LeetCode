import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        # 683ms - 700ms
        ans = 0
        for num in range(low, high + 1):
            s_num = list(str(num))
            t, len_s = 0, len(s_num)
            for j in range(len_s//2):
                t += int(s_num[j]) - int(s_num[len_s - j - 1])
            if len_s % 2 == 0 and t == 0:
                ans += 1
        return ans

    def countSymmetricIntegers2(self, low: int, high: int) -> int:
        # 716ms - 729ms
        ans = 0
        for num in range(low, high + 1):
            arr = []
            for k in str(num):
                arr.append(int(k))
            length = len(arr)
            n = length // 2
            if length > 0 and length%2 == 0 and sum(arr[n:]) == sum(arr[:n]):
                ans += 1
        return ans

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

    low, high = int(flds[0]), int(flds[1])
    print("low = {0:d}, high = {1:d}".format(low, high))

    sl = Solution()
    time0 = time.time()

    result = sl.countSymmetricIntegers(low, high)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
