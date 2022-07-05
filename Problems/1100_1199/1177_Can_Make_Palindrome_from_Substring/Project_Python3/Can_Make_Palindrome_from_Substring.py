# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        # 1368ms
        letter_occurrences = [0] * 26
        bit_values = []
        bit_value = 1
        odd_value = 0
        odd_values = []
        ret = []

        for i in range(31):
            bit_values.append(bit_value)
            bit_value *= 2

        for letter in s:
            index = ord(letter) - 97
            letter_occurrences[index] += 1
            if (letter_occurrences[index] & 1):
                odd_value += bit_values[index]
            else:
                odd_value -= bit_values[index]
            odd_values.append(odd_value)

        for query in queries:
            length = query[1] - query[0] + 1
            if (length <= 2 * query[2]):
                ret.append(True)
            else:
                if query[0] > 0:
                    odd_value = odd_values[query[1]] ^ odd_values[query[0] - 1]
                else:
                    odd_value = odd_values[query[1]]

                odds = bin(odd_value).count("1") - 1 if length & 1 else bin(odd_value).count("1")

                if (odds % 2 == 0 and odds // 2 <= query[2]):
                    ret.append(True)
                else:
                    ret.append(False)
        return ret

    def canMakePaliQueries2(self, s: str, queries: List[List[int]]) -> List[bool]:
        # 2408ms
        cnt = [[0] * 26]
        for i, c in enumerate(s):
            cnt.append(cnt[i][:])
            cnt[i + 1][ord(c) - ord('a')] += 1
        return [sum((cnt[hi + 1][i] - cnt[lo][i]) % 2 for i in range(26)) // 2 <= k for lo, hi, k in queries]

    def canMakePaliQueries2_detail(self, s: str, queries: List[List[int]]) -> List[bool]:
        # 2288ms
        cnt = [[0] * 26]
        for i, c in enumerate(s):
            cnt.append(cnt[i][:])
            cnt[i + 1][ord(c) - ord('a')] += 1

        res = []
        for lo, hi, k in queries:
            count = 0
            for i in range(26):
                count += (cnt[hi + 1][i] - cnt[lo][i]) % 2
            res.append(count//2 <= k)
        return res


    def canMakePaliQueries_bad(self, s: str, queries: List[List[int]]) -> List[bool]:
        res = []
        for query in queries:
            target = s[query[0]:query[1] + 1]
            res.append(self.isPalindrome(target, query[2]))
        return res

    def isPalindrome(self, s: str, k: int) -> bool:
        print(s, k)
        if len(s) == 1:
            return True
        for i in range(0, len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                k -= 1
                if k < 0:
                    return False
        return True

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
    flds = temp.replace(" ", "").replace("\"", "").rstrip().split("],[[")

    s = flds[0].replace("[[", "")
    print("s = {0}".format(s))

    queries = [[int(col) for col in data.split(",")] for data in flds[1].replace("]]]", "").split("],[")]
    print("queries = {0}".format(queries))

    sl = Solution()
    time0 = time.time()

    result = sl.canMakePaliQueries(s, queries)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
