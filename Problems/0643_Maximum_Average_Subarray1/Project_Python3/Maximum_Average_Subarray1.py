import itertools
import os
import operator
import sys
import time

class Solution:
    def findMaxAverage2(self, nums: 'List[int]', k: 'int') -> 'float':
        sums = [0] + list(itertools.accumulate(nums))
        return max(map(operator.sub, sums[k:], sums)) / k

    def findMaxAverage(self, nums, k):
        current_mean = sum(nums[:k])
        max_mean = current_mean
        
        for i in range(len(nums) - k):
            current_mean -= nums[i]
            current_mean += nums[i + k]
            
            if current_mean > max_mean:
                max_mean = current_mean
            
        return max_mean / k

def str_to_int_array(flds):
    if len(flds) <= 0:
        return None
    temp = flds.split(",")
    nums = [0]*len(temp)
    for i in range(len(temp)):
        nums[i] = int(temp[i])
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
        temp = temp.strip()
        if temp == "":
            continue
        print("argv[1] = %s" %temp)
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    nums = str_to_int_array(str_args[0])
    k = int(str_args[1])
    print("nums[] = %s, k = %d" %(nums, k))

    time0 = time.time()

    sl = Solution()
    result = sl.findMaxAverage(nums, k)

    print("result = %s" %result)

    time1 = time.time()
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
