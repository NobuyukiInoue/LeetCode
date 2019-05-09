# coding: utf-8

import os
import sys
import time

class Solution:

#    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
    def findRestaurant(self, list1, list2):
        Aindex = {u: i for i, u in enumerate(list1)}
        best, ans = 1e9, []

        for j, v in enumerate(list2):
            i = Aindex.get(v, 1e9)
            if i + j < best:
                best = i + j
                ans = [v]
            elif i + j == best:
                ans.append(v)
        return ans

#    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
    def findRestaurant2(self, list1, list2):
        m = len(list1)
        n = len(list2)
        
        if m>n:
            list1, list2 = list2, list1

        dic = {}
        for i in range(len(list1)):
            if not list1[i] in dic.keys():
                dic[list1[i]] = i
            else:
                print("error!!..")
        min_sum_index = sys.maxsize
        for j in range(len(list2)):
            if list2[j] in dic.keys():
                if j + dic[list2[j]] < min_sum_index:
                    min_sum_index = j + dic[list2[j]]
                    result = [list2[j]]
                elif j + dic[list2[j]] == min_sum_index:
                    result.append(list2[j])
        return result

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
        print("args = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    flds = temp.replace("\"","").replace(" ","").replace("[[","").replace("]]","").rstrip().split("],[")
    list1 = flds[0].split(",")
    list2 = flds[1].split(",")
    print("list1 = %s" %list1)
    print("list2 = %s" %list2)

    time0 = time.time()

    sl = Solution()
    result = sl.findRestaurant(list1, list2)

    time1 = time.time()

    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
