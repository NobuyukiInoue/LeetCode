import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:

    def originalDigits(self, s: str) -> str:
        # 36ms
        res = ""
        res += "0"*s.count('z')
        res += "1"*(s.count('o')-s.count('z')-s.count('w')-s.count('u'))
        res += "2"*s.count('w')
        res += "3"*(s.count('h') - s.count('g'))
        res += "4"*s.count('u')
        res += "5"*(s.count('f') - s.count('u'))
        res += "6"*s.count('x')
        res += "7"*(s.count('s')-s.count('x'))
        res += "8"*s.count("g")
        res += "9"*(s.count('i') - s.count('x') - s.count("g") - s.count('f') + s.count('u'))
        return res

    def originalDigits2(self, s: str) -> str:
        # 48ms
        l, cnt, ret = [('zero','z'), ('one','o'), ('two','w'), ('three','h'), ('four','u'), ('five','f'), ('six','x'), ('seven','s'), ('eight','g'), ('nine','i')], collections.Counter(s), []
        for i in [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]:
            n = cnt[l[i][1]]
            for c in l[i][0]:
                cnt[c] -= n
            ret += [str(i)]*n
        return ''.join(sorted(ret))

    def originalDigits3(self, s: str) -> str:
        # 400ms
        numbers = [('zero', 0), ('two', 2), ('eight', 8), ('four', 4), ('one', 1), ('three', 3), ('five', 5), ('six', 6), ('seven', 7), ('nine', 9)]
        res, S = [], collections.Counter(s)
        for n in numbers:
            c = collections.Counter(n[0])
            while c&S == c:
                res.append(n[1])
                S -= c
        return ''.join([str(i) for i in sorted(res)])


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

    result = sl.originalDigits(s)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
