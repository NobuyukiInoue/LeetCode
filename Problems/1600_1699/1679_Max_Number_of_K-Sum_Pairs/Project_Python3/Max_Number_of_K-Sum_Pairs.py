import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # 648ms - 659ms
        nums.sort()
        low , high, minOperations = 0, len(nums) - 1, 0
        while low < high:
            if nums[low] + nums[high] == k:
                low += 1
                high -= 1
                minOperations += 1
            elif nums[low] + nums[high] > k:
                high -= 1
            else:
                low += 1
        return minOperations

    def maxOperations2(self, nums: List[int], k: int) -> int:
        # 622ms - 660ms
        cnt, ans = collections.Counter(nums), 0
        for val in cnt:
            ans += min(cnt[val], cnt[k - val])
        return ans//2

    def maxOperations_bad(self, nums: List[int], k: int) -> int:
        n, res = len(nums), 0
        check = [False for _ in nums]
        for i in range(n - 1):
            if check[i]:
                continue
            for j in range(i + 1, n):
                if nums[i] + nums[j] != k:
                    continue
                res += 1
                check[j] = True
                break
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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")

    nums = [int(n) for n in flds[0].split(",")]
    k = int(flds[1])
    print("nums = {0}, k = {1:d}".format(nums, k))

    sl = Solution()
    time0 = time.time()

    result = sl.maxOperations(nums, k)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
