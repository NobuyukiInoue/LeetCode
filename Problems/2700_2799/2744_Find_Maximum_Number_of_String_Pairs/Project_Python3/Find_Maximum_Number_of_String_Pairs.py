import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        # 56ms - 61ms
        word_set = []
        ans = 0
        for word in words:
            if word in word_set:
                ans += 1
            else:
                word_set.append(word[::-1])
        return ans

    def maximumNumberOfStringPairs_use_dic(self, words: List[str]) -> int:
        # 62ms - 65ms
        dic = collections.defaultdict(int)
        for word in words:
            dic[min(word, word[::-1])] += 1
        return  sum(map((lambda x: x*(x-1)), dic.values()))//2

    def maximumNumberOfStringPairs2(self, words: List[str]) -> int:
        # 69ms - 72ms
        ans, n = 0, len(words)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if words[i] == words[j][::-1]:
                    ans += 1
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
    words = temp.replace("\"", "").replace("[", "").replace("]", "").rstrip().split(",")
    print("words = {0}".format(words))

    sl = Solution()
    time0 = time.time()

    result = sl.maximumNumberOfStringPairs(words)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
