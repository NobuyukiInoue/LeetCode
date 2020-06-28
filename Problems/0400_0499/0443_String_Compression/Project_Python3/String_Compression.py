# coding: utf-8

import os
import sys
import time
from itertools import groupby

class Solution:
#   def compress(self, chars: List[str]) -> int:
    def compress(self, chars):
        # 60ms
        left = i = 0
        while i < len(chars):
            char, length = chars[i], 1
            while (i + 1) < len(chars) and char == chars[i + 1]:
                length, i = length + 1, i + 1
            chars[left] = char
            if length > 1:
                len_str = str(length)
                chars[left + 1:left + 1 + len(len_str)] = len_str
                left += len(len_str)
            left, i = left + 1, i + 1
        return left

    def compress2(self, chars):
        # 64ms
        chars.append("0")
        p, count, j, ans = chars[0], 0, 0, 0
        for i, ch in enumerate(chars):
            if ch == p:
                count += 1
            if ch != p:
                if count > 1:
                    chars[j] = p
                    ans += 1
                    j +=  1
                    for digit in str(count):
                        chars[j] = digit
                        ans +=  1
                        j +=  1
                elif count == 1:
                    chars[j] = p
                    ans +=  1
                    j +=  1
                count, p = 1, ch
        return ans

    def compress3(self, chars):
        # 64ms
        i = 0
        for x,gx in groupby(chars):
            chars [i] = x
            i += 1
            n = 0
            for _ in gx:
                n += 1
            if n > 1:
                for x in str (n):
                    chars [i] = x
                    i += 1
        return i

    def compress_bad(self, chars):
        i = 0
        while i < len(chars):
            j = i + 1
            while j < len(chars):
                if chars[i] != chars[j]:
                    break
                j += 1
            if j - i > 1:
                chars = chars[:i + 1] + [str(j - i)] + chars[j:]
            i += 1 + len(str(j - i))
        return len(chars)

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
    date = temp.replace("[","").replace("]","").replace(", ",",").replace("\"","").rstrip()
    chars = date.split(",")
    print("chars = {0}".format(chars))
    sl = Solution()
    time0 = time.time()
    result = sl.compress(chars)

    time1 = time.time()

    print("result = {0}, chars = {1}".format(result, chars))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
