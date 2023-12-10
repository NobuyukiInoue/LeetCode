import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        # 58ms - 68ms
        return [i for i, word in enumerate(words) if x in word]

    def findWordsContaining2(self, words: List[str], x: str) -> List[int]:
        # 63ms - 72ms 
        return [i for i in range(len(words)) if x in words[i]]

    def findWordsContaining3(self, words: List[str], x: str) -> List[int]:
        # 72ms
        ans = []
        for i, word in enumerate(words):
            if x in word:
                ans.append(i)
        return ans

    def findWordsContaining4(self, words: List[str], x: str) -> List[int]:
        # 53ms - 66ms
        ans = []
        for i in range(len(words)):
            if x in words[i]:
                ans.append(i)
        return ans

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
    flds = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").rstrip().split("],[")
    words, x = flds[0].split(","), flds[1]
    print("words = {0}, x = \"{1}\"".format(words, x))

    sl = Solution()
    time0 = time.time()

    result = sl.findWordsContaining(words, x)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
