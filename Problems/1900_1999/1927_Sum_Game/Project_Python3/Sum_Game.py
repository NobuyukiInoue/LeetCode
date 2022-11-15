import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def sumGame(self, num: str) -> bool:
        # 163ms - 301ms
        n = len(num)
        q_cnt_1 = s1 = 0
        for i in range(n//2):
            if num[i] == '?':
                q_cnt_1 += 1
            else:    
                s1 += int(num[i])
        q_cnt_2 = s2 = 0				
        for i in range(n//2, n):
            if num[i] == '?':
                q_cnt_2 += 1
            else:    
                s2 += int(num[i])
        s_diff = s1 - s2
        q_diff = q_cnt_2 - q_cnt_1
        return not (q_diff % 2 == 0 and q_diff // 2 * 9 == s_diff)

    def sumGame2(self, num: str) -> bool:
        # 235ms - 572ms
        len_num, res = len(num), 0.0
        for i, _ in enumerate(num):
            if i < len_num // 2:
                res1 = 1
            else:
                res1 = -1
            if num[i] == "?":
                res += res1*4.5
            else:
                res += res1*(ord(num[i]) - ord('0'))
        return res != 0

    def sumGame_1liner(self, num: str) -> bool:
        # 425ms - 988ms
        return sum([1, -1][i < len(num) / 2] * (4.5 if c == '?' else int(c)) for i, c in enumerate(num)) != 0

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
    print("num = {0}".format(num))

    sl = Solution()
    time0 = time.time()

    result = sl.sumGame(num)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
