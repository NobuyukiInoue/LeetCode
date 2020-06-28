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
    flds = temp.rstrip().replace("[[", "").replace("]]", "").split("],[")

    nums1 = [int(val) for val in flds[0].split(",")]
    nums2 = [int(val) for val in flds[1].split(",")]
    print("nums1 = {0}".format(nums1))
    print("nums2 = {0}".format(nums2))

    sl = Solution()
    time0 = time.time()

    result = sl.intersect(nums1, nums2)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
