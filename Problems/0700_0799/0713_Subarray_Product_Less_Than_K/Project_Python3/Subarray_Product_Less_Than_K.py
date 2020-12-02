# coding: utf-8

import json
import os
import sys
import time

class Solution:
#   def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
    def numSubarrayProductLessThanK(self, nums: [int], k: int) -> int:
        # 1052ms
        if k <= 1:
            return 0
        left = 0
        count = 0
        prod = 1
        for right in range(len(nums)):
            prod *= nums[right]
            while prod >= k:
                prod //= nums[left]
                left += 1
            count += right - left + 1
        return count

    def numSubarrayProductLessThanK2(self, nums: [int], k: int) -> int:
        # 1068ms
        if len(nums) == 1:
            return 1 if nums[0] < k else 0
        cur_prod = 1
        j = 0
        res = 0
        for i, n in enumerate(nums):
            cur_prod *= n
            while cur_prod >= k and j <= i:
                cur_prod /= nums[j]
                j += 1
            res += 1 + (i - j)
        return res

    def numSubarrayProductLessThanK3(self, nums: [int], k: int) -> int:
        # 1184ms
        if k == 0:
            return 0
        start, prod, cnt = 0, 1, 0
        for end in range(len(nums)):
            while start <= end and prod*nums[end] >= k:
                prod = prod/nums[start]
                start += 1
            prod = 1 if start > end else prod*nums[end]
            cnt = cnt if start > end else cnt+(end - start + 1)
        return cnt

    def numSubarrayProductLessThanK_bad(self, nums: [int], k: int) -> int:
        res = []
        def dfs(nums: [int], k: int):
            numsLen = len(nums)
            if numsLen == 1:
                if nums[0] < k and nums not in res:
                    res.append(nums)
                return
            prod = 1
            for i in range(numsLen):
                prod *= nums[i]
            if prod < k and nums not in res:
                res.append(nums)
            if numsLen == 2:
                dfs([nums[0]], k)
                dfs([nums[1]], k)
            elif numsLen > 2:
                dfs(nums[1:], k)
                dfs(nums[:-1], k)
        dfs(nums, k)
        print("res = {0}".format(res))
        return len(res)


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
    nums, k = [int(n) for n in flds[0].split(",")], int(flds[1])
    print("nums = {0}, k = {1}".format(nums, k))

    sl = Solution()
    time0 = time.time()

    result = sl.numSubarrayProductLessThanK(nums, k)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
