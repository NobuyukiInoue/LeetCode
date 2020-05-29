# coding: utf-8

import os
import operator
import sys
import time

class Solution:
#   def maxVowels(self, s: str, k: int) -> int:
    def maxVowels(self, s, k):
        # 124ms
        count = 0
        targetChars = "aeiou"
        for i in range(k):
            if i >= len(s):
                break
            if s[i] in targetChars:
                count += 1
        maxCount = count
        for i in range(k, len(s)):
            if s[i - k] in targetChars:
                count -= 1
            if s[i] in targetChars:
                count += 1
            if count > maxCount:
                maxCount = count
        return maxCount

    def maxVowels2(self, s, k):
        # 204ms
        vowels = set('aeiou')
        curr = ans = 0
        for i, c in enumerate(s):
            curr += (c in vowels) - (i >= k and s[i-k] in vowels)
            ans = max(ans, curr)
        return ans

    def maxVowels_old(self, s, k):
        # 300ms
        count = 0
        for i in range(k):
            if i >= len(s):
                break
            if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u":
                count += 1
        maxCount = count
        for i in range(k, len(s)):
            if s[i - k] == "a" or s[i - k] == "e" or s[i - k] == "i" or s[i - k] == "o" or s[i- k] == "u":
                count -= 1
            if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u":
                count += 1
            if count > maxCount:
                maxCount = count
        return maxCount


def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
        print("Usage: python %s <testdata.txt>" %(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("%s not found..." %argv[1])
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        temp = temp.strip()
        if temp == "":
            continue
        print("args = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    flds = temp.replace("[[","").replace("]]","").rstrip().split("],[")

    s = flds[0].replace("\"","")
    k = int(flds[1])
    print("s = \"{0}\", k = {1:d}".format(s, k))
  
    time0 = time.time()

    sl = Solution()
    result = sl.maxVowels(s, k)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
