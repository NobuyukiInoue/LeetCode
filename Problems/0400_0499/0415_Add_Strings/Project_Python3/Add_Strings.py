import os
import sys
import time

class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if(len(num1)>=len(num2)):
            length = len(num1) 
            num2 = num2.rjust(length, '0') 
        else: 
            length = len(num2) 
            num1 = num1.rjust(length, '0') 
        
        suffix = ''
        carry = 0
        for i in range(length)[::-1]:
            suffix += str((int(num1[i]) + int(num2[i]) + carry) % 10)
            carry = int((int(num1[i]) + int(num2[i]) + carry)/10)

        if(carry>0):
            suffix = str(carry) + suffix[::-1]
        else:
            suffix = suffix[::-1]
        return(suffix)

    def addStrings_work(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) > len(num2):
            results_length = len(num1) + 1
        else:
            results_length = len(num2) + 1
        results = ['0']*results_length
        i = len(num1) - 1
        j = len(num2) - 1
        k = results_length - 1
        while i >= 0 or j >= 0 or k >= 0:
            sum = 0
            if i >= 0:
                sum += ord(num1[i]) - 0x30
                i -= 1
            if j >= 0:
                sum += ord(num2[j]) - 0x30
                j -= 1
            if k >= 0:
                sum += ord(results[k]) - 0x30
            results[k] = chr(sum % 10 + 0x30)
            if k > 0:
                results[k - 1] = chr(sum // 10 + 0x30)
            k -= 1

        if results[0] == '0':
            return ''.join(results[1:])
        else:
            return ''.join(results)

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
    nums1 = flds[0]
    nums2 = flds[1]
    print("nums1 = {0}\nnums2 = {1}".format(nums1, nums2))

    sl = Solution()
    time0 = time.time()
    result = sl.addStrings(nums1, nums2)

    print("result = {0}".format(result))

    time1 = time.time()
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
