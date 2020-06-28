import os
import sys
import time

class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        neg=( (dividend < 0 or divisor < 0) and not (dividend < 0 and divisor < 0) )

        x, y = abs(dividend), abs(divisor)

        zgen=range(y,x,y)
        zlen=len(zgen)
            
        if y > x:
            return 0
        if x == y:
            return -1 if neg else 1

        if zgen[-1] + y <= x:
            zlen+=1

        if neg:
            return 0 - zlen
        return min(max(-2147483648,zlen),2147483647)

    def divide_work(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        result = 0

        if dividend*divisor >= 0: 
            isPositive = 1
        else:
            isPositive = -1

        dividend, divisor = abs(dividend), abs(divisor)
        div_list = [divisor*100000 , divisor*10000, divisor*1000, divisor*100, divisor*10, divisor]

        for temp in div_list:
            while dividend - temp >= 0:
                dividend -= temp
                result += (temp // divisor)

        result *= isPositive
        if result < -(2 ** 31):
            return -(2 ** 31)
        elif result > (2 ** 31 - 1):
            return (2 ** 31 - 1)
        else:
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
    flds = temp.replace("\"","").replace("[","").replace("]","").rstrip().split(",")
    dividend, divisor = int(flds[0]), int(flds[1])

    sl = Solution()
    time0 = time.time()

    result = sl.divide(dividend, divisor)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
