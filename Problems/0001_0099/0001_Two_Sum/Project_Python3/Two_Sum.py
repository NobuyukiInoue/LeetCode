import os
import sys
import time

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        store = dict()
        for i in range(len(nums)):
            search = target - nums[i]
            if search in store:
                return [store[search],i]
            else:
                store[nums[i]] = i 
        return 0

    def twoSum_work(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = [0]*2
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    result[0] = i
                    result[1] = j
                    return result
        return result
    
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
    target = int(str_args[1])
    print("nums[] = %s, target = %d" %(nums, target))

    time0 = time.time()

    sl = Solution()
    result = sl.twoSum(nums, target)

    print("result = %s" %result)

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()


if __name__ == "__main__":
    main()
