import os
import sys
import time

class Solution:
    def Climb_Stairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] + [1] + [2] + [0] * (n - 2)
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

    def Climb_Stairs1(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.resultArray = [-1]*(n + 1)
        return self.calc_next1(n)

    def Climb_Stairs2(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.resultArray = [-1]*(n + 1)
        self.resultArray[0] = 0
        if n >= 1:
            self.resultArray[1] = 1
        if n >= 2:
            self.resultArray[2] = 2
        return self.calc_next2(n)

    def calc_next2(self, n):
        if self.resultArray[n] >= 0:
            return self.resultArray[n]
        sum = 0
        if n == 1:
            sum += 1
        else:
            sum += self.calc_next2(n - 1)
        if n == 2:
            sum += 1
        else:
            sum += self.calc_next2(n - 2)
        self.resultArray[n] = sum
        return sum

    def calc_next1(self, n):
        if self.resultArray[n] >= 0:
            return self.resultArray[n]
        sum = 0
        for i in range(1, 3):
            if i == n:
                sum += 1
                break
            if i > n:
                break
            sum += self.calc_next1(n - i)

        self.resultArray[n] = sum

        # print("result[%d] = %d" %(n, sum))
        return sum
    
    def print_resultArray(self, n):
        for i in range(0, len(self.resultArray)):
            print("resultArray[%d] = %d" %(i, self.resultArray[i]))

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
        print("args = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()


def loop_main(temp):
    str_args = temp.replace("\"","").replace("[","").replace("]","").rstrip()
    n = int(str_args)
    print("n = %d" %n)

    time0 = time.time()

    sl = Solution()
    result = sl.Climb_Stairs(n)

    print("result = %s" %result)

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()


if __name__ == "__main__":
    main()
