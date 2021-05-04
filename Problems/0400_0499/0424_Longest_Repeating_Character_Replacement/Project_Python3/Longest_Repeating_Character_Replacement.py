import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 84ms
        if len(s) == 0:
            return 0
        max_char, max_val, left = "", 0, 0
        counter = collections.defaultdict(int)
        for i, ch in enumerate(s):
            counter[ch] += 1
            if counter[ch] > max_val: 
                max_val = counter[ch]
                max_char = ch
            new_k = k - (i - left + 1 - max_val)
            if new_k < 0:
                counter[s[left]] -= 1
                if s[left] == max_char:
                    max_val -= 1
                left += 1
        return i - left + 1

    def characterReplacement3(self, s: str, k: int) -> int:
        # 116ms
        maxf = res = 0
        count = collections.Counter()
        for i in range(len(s)):
            count[s[i]] += 1
            maxf = max(maxf, count[s[i]])
            if res - maxf < k:
                res += 1
            else:
                count[s[i - res]] -= 1
        return res

    def characterReplacement2(self, s: str, k: int) -> int:
        # 116ms
        m = [0]*52
        maxWindowChar = 0
        start, maxSize = 0, 0
        for i, c in enumerate(s):
            m[ord(c) - ord('A')] += 1
            if m[ord(c) - ord('A')] > maxWindowChar:
                maxWindowChar = m[ord(c) - ord('A')]
            if i - start + 1 - maxWindowChar > k:
                m[ord(s[start]) - ord('A')] -= 1
                start += 1
            if i - start + 1 > maxSize:
                maxSize = i - start + 1
        return maxSize

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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    s, k = flds[0], int(flds[1])
    print("s = \"{0}\", k = {1:d}".format(s, k))

    sl = Solution()
    time0 = time.time()

    result = sl.characterReplacement(s, k)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
