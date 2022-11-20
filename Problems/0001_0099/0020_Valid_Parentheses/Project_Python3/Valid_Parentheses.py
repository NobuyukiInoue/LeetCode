import os
import sys
import time

from typing import List, Dict, Tuple

class Solution:
    def isValid(self, s: str) -> bool:
        # 34ms - 36ms
        dic = {'(':1 , ')':2 , '[':3 , ']':6 , '{':5 , '}':10}
        res = []
        for ch in s:
            temp = dic[ch]
            if temp%2:
                res.append(temp)
            else:
                if len(res) and res[-1] == temp//2:
                    del res[-1]
                else:
                    return False
        return res == []

    def isValid2(self, s: str) -> bool:
        # 58ms - 66ms
        stack = [0]*len(s)
        n = 0
        for ch in s:
            if n < 0:
                return False
            if ch == "(":
                stack[n] = ch
                n += 1
            elif ch == "{":
                stack[n] = ch
                n += 1
            elif ch == "[":
                stack[n] = ch
                n += 1
            elif n > 0:
                if ch == ")" and stack[n - 1] == "(":
                    n -= 1
                elif ch == "}" and stack[n - 1] == "{":
                    n -= 1
                elif ch == "]" and stack[n - 1] == "[":
                    n -= 1
                else:
                    return False
            else:
                return False
        return n == 0

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
    s = temp.replace("\"","").rstrip()
    print("s = {0}".format(s))

    sl = Solution()
    time0 = time.time()

    result = sl.isValid(s)

    time1 = time.time()
    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
