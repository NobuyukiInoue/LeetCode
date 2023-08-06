import functools
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        # 288ms - 297ms
        low = "0"*(len(high) - len(low)) + low
        mod = 10**9 + 7
        @functools.lru_cache(None)
        def dfs(i: int, is_greater_thn_low: bool, is_less_thn_high: bool, prev_digit:int ,nonzero:bool):
            if i == len(high):
                return 1
            total = 0
            start = int(low[i]) if not is_greater_thn_low else 0
            end = int(high[i]) + 1 if not is_less_thn_high else 10
            for nx_digit in range(start,end):
                if not nonzero or abs(prev_digit - nx_digit) == 1:
                    total += dfs(i + 1,is_greater_thn_low or nx_digit > int(low[i]), is_less_thn_high or nx_digit < int(high[i]), nx_digit,nonzero or nx_digit != 0)
            return total%mod
        return dfs(0, False, False, -1, False)

    def countSteppingNumbers_bad(self, low: str, high: str) -> int:
        MOD = 1_000_000_000 + 7
        def get_diff_abs(num: int):
            s_num = list(str(num))
            s_num_len = len(s_num)
            if s_num_len == 1:
                return 1
            df = 0
            prev = int(s_num[0])
            for i in range(1, len(s_num)):
                temp = int(s_num[i])
                df += prev - temp
                prev = temp
            return abs(df)
        ans = 0
        i_low, i_high = int(low), int(high)
        for num in range(i_low, i_high + 1):
            if get_diff_abs(num) == 1:
                ans += 1
        return ans%MOD

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

    low, high  = flds[0], flds[1]
    print("low = {0}, high = {1}".format(low, high))

    sl = Solution()
    time0 = time.time()

    result = sl.countSteppingNumbers(low, high)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
