import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        # 35ms - 51ms
        tape_length = 0
        for i, ch in enumerate(s):
            tape_length = tape_length * int(ch) if ch.isdigit() else tape_length + 1
            if k <= tape_length:
                break
        for j in range(i, -1, -1):
            ch = s[j]
            if ch.isdigit():
                tape_length //= int(ch)
                k %= tape_length
            else:
                if k == tape_length or k == 0:
                    return ch
                tape_length -= 1

    def decodeAtIndex2(self, s: str, k: int) -> str:
        # 49ms - 56ms
        while k:
            tape_length = 0
            for _, ch in enumerate(s):
                prev = tape_length
                if ch.isalpha():
                    tape_length += 1
                    if tape_length == k:
                        return ch
                else:
                    tape_length *= int(ch)
                    if tape_length >= k:
                        k = 1 + (k - 1)%prev

    def decodeAtIndex_bad(self, s: str, k: int) -> str:
        # Too Slow.
        tape = ""
        for ch in s:
            code = ord(ch)
            if 0x30 <= code <= 0x39:
                tape = tape*(code - 0x30)
            else:
                tape += ch
        return tape[k - 1]

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

    s, k = flds[0], int(flds[1])
    print("s = {0}, k = {1:d}".format(s, k))

    sl = Solution()
    time0 = time.time()

    result = sl.decodeAtIndex(s, k)

    time1 = time.time()

    print("result = \"{0}\"".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
