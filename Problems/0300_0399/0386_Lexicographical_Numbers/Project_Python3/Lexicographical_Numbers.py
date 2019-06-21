import os
import sys
import time

class Solution:
#   def lexicalOrder(self, n: int) -> List[int]:
    def lexicalOrder(self, n):
        res, cur = [], 1
        while True:
            if cur*10 <= n:
                res.append(cur)
                cur *= 10
            else:
                ceiling = min(cur//10 * 10 + 9, n)
                res += range(cur, ceiling + 1)
                cur //= 10
                while cur and cur % 10 == 9:
                    cur //= 10
                if cur == 0:
                    break
                cur += 1
        return res

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
    n = int(temp.replace("[","").replace("]","").rstrip())
    print("n = %s" %n)

    time0 = time.time()

    sl = Solution()
    result = sl.lexicalOrder(n)

    time1 = time.time()

    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
