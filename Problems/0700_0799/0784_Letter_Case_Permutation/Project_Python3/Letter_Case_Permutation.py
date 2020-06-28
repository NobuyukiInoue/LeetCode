# coding: utf-8

import itertools
import os
import sys
import time

class Solution:
#    def letterCasePermutation(self, S: str) -> List[str]:
    def letterCasePermutation(self, S: 'str') -> 'List[str]':
        # 72ms
        res = ['']
        for i in range(len(S)):        
            res = [_ + S[i] for _ in res] if S[i].isdigit() else [_ + j for _ in res for j in (S[i].lower(), S[i].upper())]
        return res

    def letterCasePermutation2(self, S):
        # 72ms
        L = [[i.lower(), i.upper()] if i.isalpha() else i for i in S]
        return [''.join(i) for i in itertools.product(*L)]

    def letterCasePermutation3(self, S):
        # 72ms
        res = ['']
        for ch in S:
            if ch.isalpha():
                res = [i+j for i in res for j in [ch.upper(), ch.lower()]]
            else:
                res = [i+ch for i in res]
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
    S = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    print("S = {0}".format(S))

    sl = Solution()
    time0 = time.time()
    result = sl.letterCasePermutation(S)

    time1 = time.time()
    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
