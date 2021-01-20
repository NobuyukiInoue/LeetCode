# coding: utf-8

import copy
import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def sortArray_default(self, nums: List[int]) -> List[int]:
        # 160ms
        return sorted(nums)

    # Quick Sort
    def sortArray(self, nums: List[int]) -> List[int]:
        # 248ms
        self.quicksort(nums, 0, len(nums)-1)
        return nums

    def partition(self, nums: List[int], left: int, right: int) -> int:
        pivot = nums[right]
        start = left
        end = right - 1
        while start <= end:
            if nums[start] < pivot:
                start += 1
            elif nums[end] >= pivot:
                end -= 1
            else:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        nums[start], nums[right] = nums[right], nums[start]
        return start

    def quicksort(self, nums: List[int], left: int, right: int) -> None:
        if left >= right:
            return
        pivot = self.partition(nums, left, right)
        self.quicksort(nums, left, pivot-1)
        self.quicksort(nums, pivot+1, right)

    # Merget Sort
    def sortArray_merge(self, nums: List[int]) -> List[int]:
        # 376ms
        res = [0]*len(nums)
        self.merge_sort(nums, res, 0, len(nums))
        return res

    def merge(self, A: List[int], B: List[int], left: int, mid: int, right: int) -> None:
        i, j, k  = left, mid, 0
        while i < mid and j < right:
            if A[i] <= A[j]:
                B[k] = A[i]
                k += 1
                i += 1
            else:
                B[k] = A[j]
                k += 1
                j += 1
        if i == mid:
            while j < right:
                B[k] = A[j]
                k += 1
                j += 1
        else:
            while i < mid:
                B[k] = A[i]
                k += 1
                i += 1
        for l in range(k):
            A[left + l] = B[l]

    def merge_sort(self, A: List[int], B: List[int], left: int, right: int) -> None:
        if left == right or left == right - 1:
            return
        mid = (left + right) // 2
        self.merge_sort(A, B, left, mid)
        self.merge_sort(A, B, mid, right)
        self.merge(A, B, left, mid, right)

    # Bubble Sort
    def sortArray_bubble(self, nums: List[int]) -> List[int]:
        # Time Limit Exceeded
        work_nums = copy.deepcopy(nums)
        for i in range(len(work_nums) - 1):
            for j in range(i + 1, len(work_nums)):
                if work_nums[i] > work_nums[j]:
                    work_nums[j], work_nums[i] = work_nums[i], work_nums[j]
        return work_nums

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()

    nums   = [int(n) for n in flds.split(",")]
    print("nums = {0}".format(nums))

    sl = Solution()

    time0 = time.time()

    result = sl.sortArray(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
