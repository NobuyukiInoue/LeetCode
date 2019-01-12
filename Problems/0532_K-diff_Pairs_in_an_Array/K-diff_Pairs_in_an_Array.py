import collections
import os
import sys
import time

class Solution:
    def findPairs(self, nums, k):
        if k < 0:
            return 0
        
        if k == 0:
            sorted_nums = sorted(nums)
            out = set()
            prev = None
            for element in sorted_nums:
                if element != prev:
                    prev = element
                    continue
                if element in out:
                    continue
                out.add(element)
            
            return len(out)
        
        nums_set = set(nums)
        
        cnt = 0
        for element in nums_set:
            if (element + k) in nums_set:
                cnt += 1
        
        return cnt

    def findPairs2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        count, pre_num_i, pre_num_j = 0, -sys.maxsize, -sys.maxsize
        for i in range(len(nums)):
            if nums[i] == pre_num_i:
                continue
            pre_num_i = nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == pre_num_j:
                    continue
                pre_num_j = nums[j]
                if abs(nums[i] - nums[j]) == k:
                    count += 1
            pre_num_j = -sys.maxsize
        return count

def str_to_int_array(flds):
    data = flds.split(",")
    nums = [0]*len(data)

    if (len(data) <= 0):
        return []
    for i in range((len(data))):
        nums[i] = int(data[i])

    return nums

def main():
    argv = sys.argv
    argc = len(argv)

    if (argc < 2):
        print("Usage: python %s <testdata.txt>" %(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("%s not found..." %argv[1])
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        print("argv[1] = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").rstrip().split("],[")
    nums = str_to_int_array(flds[0])
    k = int(flds[1])

    time0 = time.time()

    sl = Solution()
    result = sl.findPairs(nums, k)

    print("result = %d" %result)

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
