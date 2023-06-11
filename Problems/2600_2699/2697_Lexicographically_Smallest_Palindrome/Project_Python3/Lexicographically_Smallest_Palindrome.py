import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        # 134ms - 136ms
        pal = ''.join([min(a, b) for a, b in zip(s[:len(s)//2], s[::-1])])
        return pal + s[len(s)//2]*(len(s)%2) + pal[::-1]

    def makeSmallestPalindrome2_1(self, s: str) -> str:
        # 134ms - 139ms
        arr_s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            if arr_s[left] < arr_s[right]:
                arr_s[right] = arr_s[left]
            elif arr_s[left] > arr_s[right]:
                arr_s[left] = arr_s[right]
            left += 1
            right -= 1
        return "".join(arr_s)

    def makeSmallestPalindrome2_2(self, s: str) -> str:
        # 178ms - 179ms
        arr_s = list(s)
        i, len_s = 0, len(s)
        while i < len_s//2:
            if arr_s[i] < arr_s[-i - 1]:
                arr_s[-i - 1] = arr_s[i]
            elif arr_s[i] > arr_s[-i - 1]:
                arr_s[i] = arr_s[-i - 1]
            i += 1
        return "".join(arr_s)

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
    print("s = \"{0}\"".format(s))

    sl = Solution()
    time0 = time.time()

    result = sl.makeSmallestPalindrome(s)

    time1 = time.time()

    print("result = \"{0}\"".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
