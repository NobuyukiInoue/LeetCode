import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def greatestLetter(self, s: str) -> str:
        # 44ms - 51ms
        capital = ord('Z')
        small = ord('z')
        while capital >= ord('A'):
            if chr(capital) in s and chr(small) in s:
                return chr(capital)
            capital -= 1
            small -= 1
        return ""

    def greatestLetter_2liner(self, s: str) -> str:
        # 56ms - 85ms
        letters = set(ch for ch in s if ch.upper() in s and ch.lower() in s)
        return "" if not letters else max(letters).upper()

    def greatestLetter_use_dic(self, s: str) -> str:
        # 53ms - 81ms
        dic = collections.defaultdict(int)
        for ch in s:
            dic[ch] += 1
        ans = 0
        for k, _ in dic.items():
            code = ord(k)
            if code <= ord('Z'):
                if chr(code + 0x20) in dic:
                    ans = max(ans, code)
        if ans == 0:
            return ""
        return chr(ans)

    def greatestLetter_use_arr(self, s: str) -> str:
        # 43ms - 76ms
        string_count = collections.Counter(s)
        best_letter = "-"
        for i in range(26):
            lower_ord = ord('a') + i
            upper_ord = ord('A') + i
            lower_letter = chr(lower_ord)
            upper_letter = chr(upper_ord)
            letter_count = min( string_count[lower_letter], string_count[upper_letter])
            if letter_count > 0 and ord( best_letter ) < upper_ord:
                best_letter = upper_letter
        if best_letter == "-":
            return ""
        return best_letter

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
    s = temp.replace("\"", "").replace("[", "").replace("]", "").rstrip()
    print("s = {0}".format(s))

    sl = Solution()
    time0 = time.time()

    result = sl.greatestLetter(s)

    time1 = time.time()

    print("result = \"{0}\"".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
