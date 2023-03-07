import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def numSplits(self, s: str) -> int:
        # 31ms
        left = sorted([s.find(l) for l in set(s)]) + [len(s)]
        right = sorted([s.rfind(l) for l in set(s)], reverse=True)+[0]
        ind = max(ind for ind in range(len(left)) if left[ind] <= right[ind])
        return min(right[ind], left[ind + 1]) - max(left[ind], right[ind + 1]) 

    def numSplits2(self, s: str) -> int:
        # 52ms - 61ms
        len_s = len(s)
        if len_s == 1:
            return 0
        elif len_s == 2:
            return 1
        first = {}
        last = {}
        for index, character in enumerate(s):
            if character not in first:
                first[character] = index
            last[character] = index
        indices = list(first.values()) + list(last.values())
        indices.sort()
        middle = len(indices)//2
        return indices[middle] - indices[middle-1]

    def numSplits3(self, s: str) -> int:
        # 210ms - 223ms
        cnts_r = collections.Counter(s)
        cnts_l = collections.defaultdict(int)
        len_l, len_r = 0, len(cnts_r.keys())
        i, ans = 0, 0
        while i < len(s) - 1:
            if not s[i] in cnts_l:
                len_l += 1
            cnts_l[s[i]] += 1
            if cnts_r[s[i]] == 1:
                len_r -= 1
            cnts_r[s[i]] -= 1
            if len_l == len_r:
                ans += 1
            i += 1
        return ans

    def numSplits4(self, s: str) -> int:
        # 189ms
        l, r = [0]*26, [0]*26
        d_l, d_r, res = 0, 0, 0
        for ch in s:
            idx = ord(ch)-ord('a')
            r[idx] += 1
            if r[idx] == 1:
                d_r += 1
        for ch in s:
            idx = ord(ch)-ord('a')
            l[idx] += 1
            if l[idx] == 1:
                d_l += 1
            r[idx] -= 1
            if r[idx] == 0:
                d_r -= 1
            if d_l == d_r:
                res += 1
        return res

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

    result = sl.numSplits(s)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
