import os
import sys
import time

class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        r_pre,c_pre=len(nums),len(nums[0])
        if r_pre*c_pre != r*c or r_pre==r and c_pre==c:
            return nums
        elements=[j for i in range(r_pre) for j in nums[i]]
        return [elements[i:i+c] for i in range(0,r*c,c)]

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
        print("argv[1] = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()


def loop_main(temp):
    args_str = temp.rstrip().split("]],")

    nums_str = args_str[0].replace("[[", "").split("],[")

    nums = []
    for i in range(len(nums_str)):
        nums.append(str_to_int_array(nums_str[i]))

    r_and_c = args_str[1].split(",")
    r = int(r_and_c[0])
    c = int(r_and_c[1])

    time0 = time.time()

    sl = Solution()
    result = sl.matrixReshape(nums, r, c)

    time1 = time.time()

    print("result = %s" %result)

    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
