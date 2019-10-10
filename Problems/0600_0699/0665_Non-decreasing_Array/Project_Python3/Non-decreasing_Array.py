# coding: utf-8

import os
import sys
import time

class Solution:
#    def checkPossibility(self, nums: List[int]) -> bool:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 60ms
        count_dec = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                count_dec += 1
                if i == 0:
                    nums[i] = nums[i + 1]
                elif nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i - 1]
                else:
                    nums[i + 1] = nums[i]
            if count_dec > 1:
                return False
        return True
    
    def checkPossibility2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 72ms
        if nums == []:
            return True

        aug_nums = [float('-inf')] + nums + [float('inf')]
        need_modified = 0
        for i in range(1, len(nums) + 1):
            if aug_nums[i] > aug_nums[i + 1]:
                if aug_nums[i + 1] < aug_nums[i - 1] and aug_nums[i] > aug_nums[i + 2]:
                    return False
                else:
                    need_modified += 1
                    if need_modified > 1:
                        return False
        
        return True

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
    flds = temp.replace("\"","").replace(" ","").replace("[","").replace("]","").rstrip().split(",")

    nums = [0]*len(flds)
    for i in range(len(flds)):
        nums[i] = int(flds[i])
    
    print("nums[] = %s" %nums)

    time0 = time.time()

    sl = Solution()
    result = sl.checkPossibility(nums)

    time1 = time.time()
    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
