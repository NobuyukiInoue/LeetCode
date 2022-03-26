# coding: utf-8

import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def findKDistantIndices_normal(self, nums: List[int], key: int, k: int) -> List[int]:
        # 140ms
        key_index = []
        for i, _ in enumerate(nums):
            if nums[i] == key:
                key_index.append(i)
        res = []
        for i, _ in enumerate(nums):
            for _, pos in enumerate(key_index):
                if abs(i - pos) <= k:
                    res.append(i)
                    break
        return res

    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        # 68ms
        ans, queue = [], collections.deque([])
        i, count = 0, k
        while i < len(nums):
            if nums[i] == key:
                while queue:
                    ans.append(queue.popleft())
                ans.append(i)
                while count > 0:
                    i += 1
                    if i > len(nums) - 1:
                        return ans
                    ans.append(i)
                    if nums[i] == key:
                        count = k + 1
                    count -= 1
                count = k
            else:
                queue.append(i)
                if len(queue) > k:
                    queue.popleft()
            i += 1
        return ans

    def findKDistantIndices_4liner(self, nums: List[int], key: int, k: int) -> List[int]:
        # 300ms
        ans = []
        n = len(nums)
        for i in range(n):
            if nums[i]==key:
                ans.extend(range(max(0, i - k), min(n, i + k + 1)))
        return list(set(ans))


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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    nums = [int(n) for n in flds[0].split(",")]
    key, k = int(flds[1]), int(flds[2])

    print("nums = {0}, key = {1:d}, k = {2:d}".format(nums, key, k))

    sl = Solution()
    time0 = time.time()

    result = sl.findKDistantIndices(nums, key, k)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
