# coding: utf-8

import collections
import os
import sys
import time

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.flag = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.result = []

#   def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    def findWords(self, board, words):
        # 360ms
        for w in words:
            self.insert(w)
        for j in range(len(board)):
            for i in range(len(board[0])):
                self.dfs(self.root, board, j, i)
        return self.result

    def insert(self, word):
        node = self.root
        for letter in word:
            node = node.children[letter]
        node.flag = True

    def dfs(self, node, board, j, i, word=''):
        if node.flag:
            self.result.append(word)
            node.flag = False
        if 0 <= j < len(board) and 0 <= i < len(board[0]):
            char = board[j][i]
            child = node.children.get(char)
            if child is not None:
                word += char
                board[j][i] = None
                self.dfs(child, board, j + 1, i, word)
                self.dfs(child, board, j - 1, i, word)
                self.dfs(child, board, j, i + 1, word)
                self.dfs(child, board, j, i - 1, word)
                board[j][i] = char

def printGrid(title, grid):
    print("{0} = [".format(title))
    for i in range(len(grid)):
        if i == 0:
            print(" [", end = "")
        else:
            print(",[", end = "")
        for j in range(len(grid[i])):
            if j == 0:
                print("{0}".format(grid[i][j]), end = "")
            else:
                print(" {0}".format(grid[i][j]), end = "")
        print("]")
    print("]")

def printResult(title, result):
    print("{0} = [".format(title))
    for i in range(len(result)):
        print(result[i])
    print("]")

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
    flds = temp.replace(" ","").replace("\"","").rstrip().split("]],[")

    board = [[col for col in data.split(",")] for data in flds[0].replace("[[[", "").split("],[")]
    printGrid("board", board)

    words = flds[1].replace("]]", "").split(",")
    print("words = {0}".format(words))

    sl = Solution()
    time0 = time.time()

    result = sl.findWords(board, words)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
