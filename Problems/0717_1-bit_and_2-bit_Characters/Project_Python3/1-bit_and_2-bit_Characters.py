import os
import sys
import time

class Solution:
#    def isOneBitCharacter(self, bits: List[int]) -> bool:
    def isOneBitCharacter(self, bits):
        i, n = 0, len(bits) - 1
        while i < n:
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        if i == n and bits[i] == 0:
            return True
        else:
            return False

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
    str_args = temp.replace(" ","").replace("\"","").replace("[","").replace("]","").rstrip()
    bits = str_to_int_array(str_args)
    print("bits[] = %s" %bits)

    time0 = time.time()

    sl = Solution()
    result = sl.isOneBitCharacter(bits)

    print("result = %s" %result)

    time1 = time.time()
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()