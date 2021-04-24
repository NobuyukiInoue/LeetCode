import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # 572ms
        out = set()
        for i in range(len(s)):
            for j in range(len(s), 0, -1):
                if i != j and j > i:
                    word = s[i:j]
                    out.add(word)
        mat = [[] for _ in range(len(s)+1)]
        mat[0] = [[]]
        for i in range(len(s)):
            for substring in out:
                if substring[::-1] == substring and s[i:i+len(substring)] == substring:
                    mat[i+len(substring)] += [j + [substring] for j in mat[i]]
        return mat[-1]

    def partition2(self, s: str) -> List[List[str]]:
        # 800ms
        return [[s[:i]] + rest
                for i in range(1, len(s)+1)
                if s[:i] == s[i-1::-1]
                for rest in self.partition(s[i:])] or [[]]

    def partition3(self, s: str) -> List[List[str]]:
        # 644ms
        n = len(s)
        res = []
        def dfs(op: List[str], k: int):
            if k == n:
                res.append(op)
                return
            for i in range(k, n):
                temp = s[k:i + 1]
                if temp == temp[::-1]:
                    dfs(op + [temp], i + 1)
        dfs([], 0)
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
    s = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    print("s = {0}".format(s))

    sl = Solution()
    time0 = time.time()

    result = sl.partition(s)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
