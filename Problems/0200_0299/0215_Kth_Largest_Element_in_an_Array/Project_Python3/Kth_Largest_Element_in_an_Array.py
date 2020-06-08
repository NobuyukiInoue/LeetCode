import os
import sys
import time

class Solution:
#   def findKthLargest(self, nums: List[int], k: int) -> int:
    def findKthLargest(self, nums, k):
        # 56ms
        nums.sort(reverse=True)
        return nums[k - 1]


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
        print("argv[1] = %s" %temp)
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()


def loop_main(temp):
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    nums = [int(val) for val in str_args[0].split(",")]
    k = int(str_args[1])

    print("nums = {0}, k = {1:d}".format(nums, k))

    time0 = time.time()

    sl = Solution()
    result = sl.findKthLargest(nums, k)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))


if __name__ == "__main__":
    main()
