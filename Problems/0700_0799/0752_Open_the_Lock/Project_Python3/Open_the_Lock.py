import collections
import os
import sys
import string
import time
from typing import List, Dict, Tuple

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 556ms
        dead_set = set(deadends)
        queue = collections.deque([('0000', 0)])
        visited = set('0000')
        while queue:
            (string, steps) = queue.popleft()
            if string == target:
                return steps
            elif string in dead_set:
                continue
            for i in range(4):
                digit = int(string[i])
                for move in [-1, 1]:
                    new_digit = (digit + move) % 10
                    new_string = string[:i]+str(new_digit)+string[i+1:]
                    if new_string not in visited:
                        visited.add(new_string)
                        queue.append((new_string, steps+1))
        return -1

    def openLock2(self, deadends: List[str], target: str) -> int:
        # 660ms
        depth = -1
        visited, q = set(deadends), collections.deque(['0000'])
        while q:
            size = len(q)
            depth += 1
            for _ in range(size):
                node = q.popleft()
                if node == target:
                    return depth
                if node in visited:
                    continue
                visited.add(node)
                q.extend(self.successors(node))
        return -1

    def successors(self, src):
        res = []
        for i, ch in enumerate(src):
            num = int(ch)
            res.append(src[:i] + str((num - 1) % 10) + src[i+1:])
            res.append(src[:i] + str((num + 1) % 10) + src[i+1:])
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

    deadends = flds[0].split(",")
    target = flds[1]

    print("deadends = {0}".format(deadends))
    print("target   = {0}".format(target))

    sl = Solution()
    time0 = time.time()

    result = sl.openLock(deadends, target)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
