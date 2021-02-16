import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 96ms
        d, b, e, bseen, eseen, L = collections.defaultdict(list), collections.deque([(beginWord,1)]), collections.deque([(endWord,1)]), {beginWord:1}, {endWord:1}, len(beginWord)
        if endWord not in wordList:
            return 0
        for i in wordList:
            for j in range(L): d[i[:j] + '-' + i[j+1:]].append(i)
        while b and e:
            cb, cbi = b.popleft()
            if cb in eseen:
                return cbi + eseen[cb] - 1
            for i in range(L):
                for j in d[cb[:i] + '-' + cb[i+1:]]:
                    if j not in bseen:
                        bseen[j] = cbi + 1
                        b.append((j,cbi + 1))
            ce, cei = e.popleft()
            if ce in bseen:
                return cei + bseen[ce] - 1
            for i in range(L):
                for j in d[ce[:i] + '-' + ce[i+1:]]:
                    if j not in eseen:
                        eseen[j] = cei + 1
                        e.append((j,cei + 1))
        return 0

    def ladderLength2(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Time Limit Exceeded.
        queue = [(beginWord, 1)]
        visited = set()
        while queue:
            word, dist = queue.pop(0)
            if word == endWord:
                return dist
            for i in range(len(word)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    tmp = word[:i] + j + word[i+1:]
                    if tmp not in visited and tmp in wordList:
                        queue.append((tmp, dist+1))
                        visited.add(tmp)
        return 0

    def ladderLength_work(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Time Limite Exceeded.
        if not endWord in wordList:
            return 0
        self.wordList = wordList
        self.endWord = endWord
        self.chkTbl = [False for _ in wordList]
        self.N = len(endWord)

#       def dfs(nextWord: str, cnt: int, arr: str) -> int:
        def dfs(nextWord: str, cnt: int) -> int:
            if nextWord == self.endWord:
#               print("arr = {0}".format(arr))
                return cnt
            res = []
            for i, _ in enumerate(wordList):
                if self.chkTbl[i]:
                    continue
                charCnt = 0
                for pos, _ in enumerate(nextWord):
                    if nextWord[pos] == wordList[i][pos]:
                        charCnt += 1
                if charCnt == self.N - 1:
                    self.chkTbl[i] = True
#                   res.append(dfs(wordList[i], cnt + 1, arr + "->" + wordList[i]))
                    res.append(dfs(wordList[i], cnt + 1))
                    self.chkTbl[i] = False
            if len(res) == 0:
                return sys.maxsize
            return min(res)

#       return dfs(beginWord, 1, beginWord)
        res = dfs(beginWord, 1)
        if res == sys.maxsize:
            return 0
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
    flds = temp.replace(", ", ",").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    beginWord = flds[0]
    endWord   = flds[1]
    wordList = flds[2].split(",")

    print("beginWord = {0}".format(beginWord))
    print("endWord   = {0}".format(endWord))
    print("wordList  = {0}".format(wordList))

    sl = Solution()
    time0 = time.time()

    result = sl.ladderLength(beginWord, endWord, wordList)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
