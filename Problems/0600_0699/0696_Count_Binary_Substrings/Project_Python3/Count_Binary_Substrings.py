# coding: utf-8

import os
import sys
import time

class Solution:
#    def countBinarySubstrings(self, s: str) -> int:
    def countBinarySubstrings(self, s):
        t = list(map(len, s.replace('01', '0 1').replace('10', '1 0').split()))
        return sum(min(a, b) for a, b in zip(t, t[1:]))

    def countBinarySubstrings_work(self, s):
        if len(s) <= 1:
            return 0
        result = 0
        for i in range(len(s)):
            target_src = s[i]
            for j in range(i + 1, len(s)):
                if s[j] != target_src:
                    break
            count1 = j - i
            if target_src == "0":
                target_nxt = "1"
            else:
                target_nxt = "0"
            flg = True
            for k in range(j, len(s)):
                count2 = k - j
                if s[k] != target_nxt:
                    flg = False
                    break
                if count2 == count1:
                    flg = False
                    break
            if flg:
                k = len(s)
                count2 = k - j
            if count1 == count2 and i != k:
                '''
                if k < j:
                    print("s[{0:d}:] = {1}".format(i, s[i:]))
                else:
                    print("s[{0:d}:{1:d}] = {2}".format(i, k, s[i:k]))
                '''
                result += 1
        return result

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
    s = temp.replace("\"","").replace(" ","").replace("[","").replace("]","").rstrip()
    print("s = {0}".format(s))

    sl = Solution()
    time0 = time.time()

    result = sl.countBinarySubstrings(s)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
