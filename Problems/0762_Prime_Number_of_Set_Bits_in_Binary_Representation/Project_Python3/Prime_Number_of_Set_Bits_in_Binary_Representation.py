import math
import os
import sys
import time

class Solution:
#    def countPrimeSetBits(self, L: int, R: int) -> int:
    def countPrimeSetBits(self, L, R):
        return self.fast_count(R+1) - self.fast_count(L)
    
    def fast_count(self, N):
        S = bin(N)
        B = [len(S) + ~i for i, b in enumerate(S) if b == '1']
        res = 0
        for p in [2, 3, 5, 7, 11, 13, 17, 19]:
            if B[0] < p: break
            for i in range(min(p+1, len(B))):
                n = B[i]; k = p - i
                if n < k: break
                res += self.binomial(n, k)
        return res

    def binomial(self, n, k, cache={}):
        if k == 0: return 1
        if (n, k) not in cache:
            cache[n, k] = self.binomial(n - 1, k - 1)*n//k
        return cache[n, k]

    def countPrimeSetBits2(self, L, R):
        # 212ms
        return sum(bin(i).count('1') in (2,3,5,7,11,13,17,19,23,29,31) for i in range(L,R+1))

    def countPrimeSetBits3(self, L, R):
        # 1212ms
        checkArray = [False]*33
        checkArray[2], checkArray[3], checkArray[5] = True, True, True
        checkArray[7], checkArray[11], checkArray[13] = True, True, True
        checkArray[17], checkArray[19], checkArray[23] = True, True, True
        checkArray[29], checkArray[31] = True, True

        toReturn = 0
        for i in range(L, R + 1):
            bitsSet, temp = 0, i
            while temp != 0:
                if temp % 2 == 1:
                    bitsSet += 1
                temp = temp >> 1
            if checkArray[bitsSet]:
                toReturn += 1
        return toReturn

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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    L = int(flds[0])
    R = int(flds[1])

    print("L = %d, R = %d\n" %(L, R))

    time0 = time.time()

    sl = Solution()
    result = sl.countPrimeSetBits(L, R)

    print("result = %d" %result)

    time1 = time.time()
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
