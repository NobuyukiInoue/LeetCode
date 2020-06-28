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
    flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").rstrip().split("],[")

    nums = [int(n) for n in flds[0].split(",")]
    k = int(flds[1])
    print("nums = {0}, k = {1:d}".format(nums, k))

    sl = Solution()
    time0 = time.time()

    result = sl.findPairs(nums, k)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
