import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # 249ms - 281ms
        if start < 0 or start >= len(arr) or arr[start] < 0:
            return False
        arr[start] *= -1
        return arr[start] == 0 or self.canReach(arr, start + arr[start]) or self.canReach(arr, start - arr[start])

    def canReach1(self, arr: List[int], start: int) -> bool:
        # 249ms - 257ms
        n = len(arr)
        visited = [False for _ in arr]
        def helper(pos: int) -> int:
            if arr[pos] == 0:
                return True
            if pos + arr[pos] < n and not visited[pos + arr[pos]]:
                visited[pos + arr[pos]] = True
                if helper(pos + arr[pos]):
                    return True
                visited[pos + arr[pos]] = False
            if pos - arr[pos] >= 0 and not visited[pos - arr[pos]]:
                visited[pos - arr[pos]] = True
                if helper(pos - arr[pos]):
                    return True
                visited[pos - arr[pos]] = False
            return False
        return helper(start)

    def canReach3(self, arr: List[int], start: int) -> bool:
        # 253ms - 274ms
        visited = [0]*len(arr)
        pos = [start]
        while pos:
            nextPos = []
            while pos:
                x = pos.pop()
                if arr[x] == 0:
                    return True
                visited[x] = 1
                for y in (x - arr[x], x + arr[x]):
                    if 0 <= y < len(arr) and not visited[y]:
                        nextPos.append(y)
            pos = nextPos
        return False

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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")

    arr = [int(n) for n in flds[0].split(",")]
    start = int(flds[1])
    print("arr = {0}, start = {1:d}".format(arr, start))

    sl = Solution()
    time0 = time.time()

    result = sl.canReach(arr, start)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
