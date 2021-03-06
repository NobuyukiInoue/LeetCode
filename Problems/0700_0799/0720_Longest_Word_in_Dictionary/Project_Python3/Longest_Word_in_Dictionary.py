import math
import os
import sys
import time

class Solution:

#    def longestWord(self, words: List[str]) -> str:
    def longestWord3(self, words):
        buckets = [[] for _ in range(30)]
        for word in words:
            buckets[len(word) - 1].append(word)
        prev, cur, ans = {''}, set(), ''
        for bucket in buckets:
            for word in bucket:
                if word[:-1] in prev:
                    cur.add(word)
                    if len(ans) < len(word) or (len(ans) == len(word) and word < ans):
                        ans = word
            prev, cur = cur, set()
        return ans

    def longestWord(self, words):
        words.sort()
        words_set, longest_word = set(['']), ''
        for word in words:
            if word[:-1] in words_set:
                words_set.add(word)
                if len(word) > len(longest_word):
                    longest_word = word
        return longest_word

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
    words = temp.replace(", ",",").replace("\"","").replace("[","").replace("]","").rstrip().split(",")
    print("words = {0}".format(words))

    sl = Solution()
    time0 = time.time()

    result = sl.longestWord(words)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
