import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def countTime(self, time: str) -> int:
        # 28ms - 62ms
        mm = (6 if time[3] == '?' else 1) * (10 if time[4] == '?' else 1)
        match [time[0], time[1]]:
            case ('?', '?'):
                return mm * 24
            case ('?', ('0' | '1' | '2' | '3')):
                return mm * 3
            case ('?', _):
                return mm * 2
            case (('0' | '1'), '?'):
                return mm * 10
            case (_, '?'):
                return mm * 4
        return mm

    def countTime_with_lambda(self, time: str) -> int:
        # 141ms - 321ms
        match = lambda s, time: all(time[i] == '?' or s[i] == time[i] for i in range(5))
        s = lambda i: str(i) if i >= 10 else '0' + str(i)
        return sum(match(s(i) +':'+ s(j), time) for i in range(24) for j in range(60))

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
    v_time = temp.replace("\"", "").replace("[", "").replace("]", "").rstrip()
    print("time = {0}".format(v_time))

    sl = Solution()
    time0 = time.time()

    result = sl.countTime(v_time)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
