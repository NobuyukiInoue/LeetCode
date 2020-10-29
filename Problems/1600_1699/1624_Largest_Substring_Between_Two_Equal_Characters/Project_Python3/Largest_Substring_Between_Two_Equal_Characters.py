import os
import sys
import time
import re

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # 20ms
        len_max = -1
        for _, ch in enumerate(s):
            len_max = max(len_max, s.rfind(ch) - s.find(ch) - 1)
        return len_max

    def maxLengthBetweenEqualCharacters2(self, s: str) -> int:
        # 28ms
        d = [-1] * 26
        ans = -1
        for i, c in enumerate(s):
            o = ord(c) - ord('a')
            if d[o] != -1:
                ans = max(ans, i - d[o] - 1)
            if d[o] == -1:
                d[o] = i
        return ans

    """
    def maxLengthBetweenEqualCharacters3(self, s: str) -> int:
        # 32ms
        return max(map(sub, range(len(s)), map({}.setdefault, s, range(1, len(s) + 1)))) 
    """

    def maxLengthBetweenEqualCharacters4(self, s: str) -> int:
        # 196ms
        len_s = len(s)
        len_max = -1
        for i, ch in enumerate(s):
            if ch != " ":
                j = i + 1
                while j < len_s and i < len_s - 1:
                    if s[j] == s[i]:
                        len_max = max(len_max, j - i - 1)
                    j += 1
                s = s.replace(ch, " ")
        return len_max

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

    result = sl.maxLengthBetweenEqualCharacters(s)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
