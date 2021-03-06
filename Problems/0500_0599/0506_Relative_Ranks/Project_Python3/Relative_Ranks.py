# coding: utf-8

import os
import sys
import time
import numpy as np

class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0: return []
        if len(nums) == 1: return ["Gold Medal"]
        if len(nums) == 2:
            if nums[0] > nums[1]: return ["Gold Medal", "Silver Medal"]
            else: return ["Silver Medal", "Gold Medal"]
        num1 = sorted(nums)[::-1]
        dic = {num: str(i+1) for i, num in enumerate(num1)}
        dic.update({num1[0]:"Gold Medal", num1[1]:"Silver Medal", num1[2]: "Bronze Medal"})
        return [dic[i] for i in nums]

    def findRelativeRanks2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        nums_ = np.array(nums)
        nums_sort = np.argsort(-nums_)
        
        nums[nums_sort[0]] = "Gold Medal"
        
        if len(nums) >= 2:
            nums[nums_sort[1]] = "Silver Medal"

        if len(nums) >= 3:
            nums[nums_sort[2]] = "Bronze Medal"
        
        if len(nums) > 3:
            for i in range(3, len(nums)):
                nums[nums_sort[i]] = str(i+1)
        
        return nums

    def findRelativeRanks_work(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) <= 0:
            return []
        '''
        sorted_nums = nums[:]
        sorted_nums.sort(reverse = True)
        '''
        sorted_nums = sorted(nums, reverse = True)
        results = [""]*len(nums)
        for n in range(len(results)):
            for i in range(len(sorted_nums)):
                if nums[n] == sorted_nums[i]:
                    if i == 0:
                        results[n] = "Gold Medal"
                    elif i == 1:
                        results[n] = "Silver Medal"
                    elif i == 2:
                        results[n] = "Bronze Medal"
                    else:
                        results[n] = str(i + 1)
        return results

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
    flds = temp.replace("[","").replace("]","").rstrip().split(",")

    nums = [int(n) for n in flds]
    print("nums = {0}".format(nums))

    sl = Solution()
    time0 = time.time()
    result = sl.findRelativeRanks(nums)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
