# coding: utf-8

import sys
import time

class Solution:
    def convertToTitle(self, n):
        if n < 1:
            return ""

        temp = n - 1
        print("temp = %s" %temp)

        target = []
        while True:
            mod = temp % 26
            print("mod = %s" %mod)
            target.append(mod)
            temp -= mod
            if temp >= 26:
                temp = int(temp / 26) - 1
                continue
            else:
                break
            
        result = ""

        for i in range(len(target)):
            result = chr(ord('A') + target[i]) + result
            print("target[%s] = %s" %(i, target[i]))
            print("result = %s" %result)

        return result


def main():
    args = sys.argv
    argc = len(args)

    print("args[0] = %s %s" %(args[0], args[1]) )

    time0 = time.time()

    sl = Solution()
    print("result = %s" %(sl.convertToTitle(int(args[1]))))

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()


if __name__ == "__main__":
    main()
