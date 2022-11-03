# coding: utf-8

import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def oddString(self, words: List[str]) -> str:
        # 44ms - 64ms
        alpha = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
        results = []
        for word in words:
            current_result = []
            for index in range(len(word) - 1):
                start = alpha[word[index]]
                end = alpha[word[index + 1]]
                current_result.append(end - start)
            results.append(current_result)
        for i, result in enumerate(results):
            if results.count(result) == 1:
                return words[i]

    def oddString2(self, words: List[str]) -> str:
        # 47ms - 68ms
        cnts = collections.defaultdict(list)
        for word in words:
            cur = ""
            for i in range(len(word) - 1):
                cur += str(ord(word[i + 1]) - ord(word[i])) + ","
            cnts[cur].append(word)
        for v in cnts.values():
            if len(v) == 1:
                return v[0]

    def oddString3(self, words: List[str]) -> str:
        # 49ms - 77ms
        cnts = collections.defaultdict(int)
        for i, word in enumerate(words):
            cur = ""
            for j in range(len(word) - 1):
                cur += str(ord(word[j + 1]) - ord(word[j])) + ","
            if cur not in cnts:
                cnts[cur] += 1
                if i == 1:
                    return self.get_ans_in_three(words, cnts)
                elif i >= 2:
                    return word
            else:
                cnts[cur] += 1
        return ""

    def get_ans_in_three(self, words: List[str], cnts: Dict[str, int]) -> str:
        cur = ""
        for j in range(len(words[2]) - 1):
            cur += str(ord(words[2][j + 1]) - ord(words[2][j])) + ","
        cnts[cur] += 1
        for i, word in enumerate(words):
            cur = ""
            for j in range(len(word) - 1):
                cur += str(ord(word[j + 1]) - ord(word[j])) + ","
            if cnts[cur] == 1:
                return word
        return ""

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
    words = temp.replace(" ","").replace("\"","").replace("[","").replace("]","").rstrip().split(",")
    print("words = {0}".format(words))
  
    sl = Solution()
    time0 = time.time()

    result = sl.oddString(words)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
