# coding: utf-8

import os
import re
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        # 976ms - 1182ms
        def helper(m):
            n = m.group(0)[1:-1]
            if n in k:
                return k[n]
            return "?"
        k = {}
        for e in knowledge:
            k[e[0]] = e[1]
        return re.sub("\((.*?)\)", helper, s)

    def evaluate_oneliner(self, s: str, knowledge: List[List[str]]) -> str:
        # 1148ms - 1369ms
        return (lambda k, z: ''.join(s[b:c] + k.get(s[c+1:d-1], '?') for (a,b),(c,d) in zip([(0,0)] + z, z)) + s[z[-1][1] if z else 0:])({k:v for k,v in knowledge}, [c.span() for c in re.finditer(r'\([a-z]*\)', s)])

    """
    def evaluate_oneliner(self, s: str, knowledge: List[List[str]]) -> str:
        d = {k:v for k,v in knowledge}
        res = []
        last = 0
        for c in finditer(r'\([a-z]*\)', s):
            a, b = c.span()
            res.append(s[last:a] + d.get(s[a+1:b-1], '?'))
            last = b
        res.append(s[last:])
        return ''.join(res)
    """
    def evaluate_work(self, s: str, knowledge: List[List[str]]) -> str:
        # Time Limit Exceeded.
        for words in knowledge:
            s = s.replace("(" + words[0] + ")", words[1])
        s = re.sub("\(.*\)", "?", s)
        """
        while "(" in s:
            pos1, pos2 = s.index("("), s.index(")")
            if pos1 >= 0 and pos2 > pos1:
                s = s[:pos1] + "?" + s[pos2 + 1:]
        """
        return s

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
    flds = temp.replace(" ","").replace("\"","").rstrip().split("],[[")

    s = flds[0].replace("[[","")
    knowledge = [data.split(",") for data in flds[1].replace("]]]","").split("],[")]
    print("s = \"{0}\", knowledge = {1}".format(s, knowledge))

    sl = Solution()
    time0 = time.time()

    result = sl.evaluate(s, knowledge)

    time1 = time.time()

    print("result = \"{0}\"".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
