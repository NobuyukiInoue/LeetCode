# coding: utf-8

import os
import sys
import time

import collections

class Solution:
#   def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
    def minHeightShelves(self, books, shelf_width):
        # 48ms
        n = len(books)
        dp = [float('inf') for _ in range(n + 1)]
        dp[0] = 0
        for i in range(1, n + 1):
            max_width = shelf_width
            max_height = 0
            j = i - 1
            while j >= 0 and max_width - books[j][0] >= 0:
                max_width -= books[j][0]
                max_height = max(max_height, books[j][1])
                dp[i] = min(dp[i], dp[j] + max_height)
                j -= 1
        return dp[n]

def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
        print("Usage: python %s <testdata.txt>" %(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("%s not found..." %argv[1])
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        temp = temp.strip()
        if temp == "":
            continue
        print("args = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    flds = temp.replace("\"","").replace("[[[","").rstrip().split("]],[")

    books_str = flds[0].split("],[")
    books = [[int(col) for col in data.split(",")] for data in books_str]
    print("books = {0}".format(books))
    shelf_width = int(flds[1].replace("]]",""))
    print("shelf_sheld = {0:d}".format(shelf_width))

    time0 = time.time()

    sl = Solution()
    result = sl.minHeightShelves(books, shelf_width)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
