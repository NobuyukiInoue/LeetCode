import itertools
import os
import sys
import time

class Solution:
#   def numTilePossibilities(self, tiles: str) -> int:
    def numTilePossibilities(self, tiles: str) -> int:
        # 40ms
        return sum(len(set(itertools.permutations(tiles, i))) for i in range(1, len(tiles) + 1))

    def numTilePossibilities1(self, tiles: str) -> int:
        # 156ms
        arr = [0]*26
        for i in range(len(tiles)):
            arr[ord(tiles[i])- ord("A")] += 1

        def helper(arr: [int]) -> int:
            sum = 0
            for i in range(26):
                if arr[i] == 0:
                    continue
                sum += 1
                arr[i] -= 1
                sum += helper(arr)
                arr[i] += 1
            return sum

        return helper(arr)

    def numTilePossibilities2(self, tiles: str) -> int:
        # 88ms
        self.count = 0
        used = [False for _ in range(len(tiles))]
        tiles = sorted(tiles)

        def backtrack(tiles: str, used: [bool]):
            self.count += 1
            for i in range(len(tiles)):
                if used[i] or i > 0 and tiles[i] == tiles[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                backtrack(tiles, used.copy())
                used[i] = False

        backtrack(tiles, used.copy())
        return self.count - 1

    def numTilePossibilities3(self, tiles: str) -> int:
        # 124ms
        def perm(s,temp,ans):
            ans.add(temp)
            for i in range(len(s)):
                perm(s[:i]+s[i+1:],temp+s[i],ans)
        ans = set()
        perm(tiles,"",ans)
        return len(ans) - 1

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
    tiles = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    print("tiles = {0}".format(tiles))

    sl = Solution()
    time0 = time.time()

    result = sl.numTilePossibilities(tiles)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
