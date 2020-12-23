import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        # 32ms
        def toUpper(s):
            return [letter for letter in s if letter.isupper()]

        def issup(pattern, que):
            it = iter(que)
            return all(letter in it for letter in pattern)

        return [toUpper(pattern) == toUpper(que) and issup(pattern, que) for que in queries]
        """
        res = []
        for que in queries:
            temp = issup(pattern, que)
            res.append(toUpper(pattern) == toUpper(que) and temp)
        return res
        """

    def camelMatch2(self, queries: List[str], pattern: str) -> List[bool]:
        # 28ms
        return [self.isCamelMatch(query, pattern) for query in queries]

    def isCamelMatch(self, query: str, pattern: str) -> bool:
        queryIndex = 0
        patternIndex = 0
        while queryIndex < len(query) and patternIndex < len(pattern):
            if query[queryIndex] != pattern[patternIndex]:
                if not query[queryIndex].islower():
                    return False
            else:
                patternIndex += 1
            queryIndex += 1
        return patternIndex == len(pattern) and all(q.islower() for q in query[queryIndex:])


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
    flds = temp.replace(", ",",").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    queries = flds[0].split(",")
    pattern = flds[1]
    print("queries = {0}".format(queries))
    print("pattern = {0}".format(pattern))

    sl = Solution()
    time0 = time.time()

    result = sl.camelMatch(queries, pattern)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
