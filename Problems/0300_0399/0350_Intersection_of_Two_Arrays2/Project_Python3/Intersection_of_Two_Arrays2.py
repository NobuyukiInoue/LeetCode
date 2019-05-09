from collections import Counter
import os
import sys
import time

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        c1, c2 = Counter(nums1), Counter(nums2)
        return sum([[num] * min(c1[num], c2[num]) for num in c1 & c2], [])

    def intersect2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d = {}
        result = []
        
        for num in nums1:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        
        for num in nums2:
            if num in d:
                if d[num] > 0:
                    d[num] -= 1
                    result.append(num)
                    
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
        print("args = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()


def loop_main(temp):
    nums_str = temp.rstrip().replace("[[", "").replace("]]", "").split("],[")
    nums1 = str_to_int_array(nums_str[0])
    nums2 = str_to_int_array(nums_str[1])

    time0 = time.time()

    sl = Solution()
    result = sl.intersect(nums1, nums2)

    time1 = time.time()

    print("result = %s" %result)

    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
