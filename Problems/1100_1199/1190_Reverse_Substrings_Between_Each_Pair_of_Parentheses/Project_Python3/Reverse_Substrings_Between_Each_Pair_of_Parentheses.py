import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def reverseParentheses(self, s: str) -> str:
        # 40ms
        res = ['']
        for c in s:
            if c == '(':
                res.append('')
            elif c == ')':
                res[len(res) - 2] += res.pop()[::-1]
            else:
                res[-1] += c
        return "".join(res)

    def reverseParentheses2(self, s: str) -> str:
        # 32ms
        def reverse(s, i = 0):
            new_word = ''
            while i < len(s):
                if s[i] == '(':
                    result, i = reverse(s, i + 1)
                    new_word += result
                elif s[i] == ')':
                    new_word = reversed(new_word)
                    new_word = ''.join([char for char in new_word])
                    return new_word, i + 1
                else:
                    new_word += s[i]
                    i += 1
            return new_word, i

        return reverse(s)[0]

    def reverseParentheses3(self, s: str) -> str:
        # 51ms
        s = list(s)
        u = []
        while s:
            a = s.pop(0)
            if a != ')':
                u.append(a)
            else:
                p = []
                while True:
                    x = u.pop()
                    if x == '(':
                        u += p
                        break
                    else:
                        p.append(x)
        return ''.join(u)

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

    result = sl.reverseParentheses(s)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
