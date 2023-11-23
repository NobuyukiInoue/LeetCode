import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        # 28ms - 35ms
        n = len(nums)
        visited = [False for _ in range(n)]
        for i in range(n):
            if visited[i]:
                continue
            index, dic = i, {}
            forward = (nums[i] >= 0)
            while True:
                visited[index] = True
                newIndex = (index + nums[index]) % n
                if newIndex < 0:
                    newIndex += n
                if index == newIndex or forward != (nums[newIndex] >= 0):
                    break
                if index in dic:
                    return True
                dic[index] = True
                index = newIndex
        return False

    def circularArrayLoop2(self, nums: List[int]) -> bool:
        # 43ms
        n, visited = len(nums), set()
        for i in range(n):
            if i in visited:
                continue
            local_s = set()
            while True:
                if i in local_s:
                    return True
                if i in visited:
                    break
                visited.add(i)
                local_s.add(i)
                prev, i = i, (i + nums[i]) % n
                if prev == i or (nums[i] > 0) != (nums[prev] > 0):
                    break
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
    flds = temp.replace("[","").replace("]","").replace(", ",",").rstrip()
    nums = [int(n) for n in flds.split(",")]
    print("nums = {0}".format(nums))

    sl = Solution()

    time0 = time.time()

    result = sl.circularArrayLoop(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
