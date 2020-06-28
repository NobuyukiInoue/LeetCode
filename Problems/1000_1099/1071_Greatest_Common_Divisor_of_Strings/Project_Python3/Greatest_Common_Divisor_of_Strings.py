import os
import sys
import time

class Solution:
#   def gcdOfStrings(self, str1: str, str2: str) -> str:
    def gcdOfStrings(self, str1, str2):
    	if len(set(str1)) != len(set(str2)):
    		return ''
    	L1, L2 = len(str1), len(str2)
    	d = self.divisors(L2)
    	d.reverse()
    	for i in d:
    		s = str2[:i]
    		if L1%i == 0 and str2 == s*int(L2/i) and str1 == s*int(L1/i):
    			return s

    def divisors(self, n):
        d, e = [], []
        for i in range(1,1+int(n**.5)):
            if n%i == 0:
                d += [i]
                e += [int(n/i)]
        e.reverse()
        if d[-1] == e[0]: del e[0]
        return(d+e)

    def gcdOfStrings2(self, str1, str2):
        # 36ms
        import math
        size = math.gcd(len(str1), len(str2))
        
        return str2[:size] if str2[:size] * (len(str1)//size) == str1 else ""

    def gcdOfStrings_bad(self, str1, str2):
        min_count = len(str1)
        for i in range(len(str1)):
            if str1[i] == str2[0]:
                count = 1
                for j in range(1, len(str2)):
                    if i + j >= len(str1):
                        break
                    if str1[i + j] == str2[j]:
                        count += 1
                if min_count > count:
                    min_count = count
        if min_count == len(str1):
            return ""
        else:
            return str2[0:min_count]

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
        print("argv[1] = {0}".format(temp))
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    flds = temp.replace(", ",",").replace("\"","").replace("[","").replace("]","").rstrip().split(",")
    str1, str2 = flds[0], flds[1]

    print("str1 = {0}, str2 = {1}".format(str1, str2))

    sl = Solution()
    time0 = time.time()
    result = sl.gcdOfStrings(str1, str2)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
