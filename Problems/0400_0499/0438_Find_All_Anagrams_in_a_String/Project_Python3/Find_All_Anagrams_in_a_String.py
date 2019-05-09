# coding: utf-8

import os
import sys
import time
import itertools

class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        n, m = len(s), len(p)
        if n < m:
            return res
        p_char_count, s_char_count = [0]*0x80, [0]*0x80
        for x in p:
            p_char_count[ord(x)] += 1
        for x in s[:m-1]:
            s_char_count[ord(x)] += 1
        for i in range(m-1, n):
            s_char_count[ord(s[i])] += 1
            if i-m >= 0:
                s_char_count[ord(s[i-m])] -= 1
            if s_char_count == p_char_count:
                res.append(i - m + 1)
        return res


    def findAnagrams_old(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        if len(s) < len(p):
            return result
        
        if len(s) > 20100 or len(p) > 20100:
            return result

        turple_match_pattern = list(itertools.permutations(p, len(p)))
    #   output_turple_match_pattern(turple_match_pattern)

        match_pattern = []
        for temp in turple_match_pattern:
            match_pattern.append(turple_to_str(temp))
    #   output_match_pattern(match_pattern)

        start = 0
        end = start + len(p)
        while end <= len(s):
            temp = s[start:end]
            for target_pattern in match_pattern:
                if temp == target_pattern:
                    result.append(start)
                    break
            start += 1
            end += 1

        return result


def turple_to_str(target):
    resultStr = ""
    for temp in target:
        resultStr += temp
    return resultStr


def output_turple_match_pattern(turple_match_pattern):
    for i in range(len(turple_match_pattern)):
        print("turple_match_pattern[%d] = %s" %(i, turple_match_pattern[i]))


def output_match_pattern(match_pattern):
    for i in range(len(match_pattern)):
        print("match_pattern[%d] = %s" %(i, match_pattern[i]))


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
    var_str = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = var_str.split("],[")
    s = flds[0]
    p = flds[1]

    print("s = %s, p = %s" %(s, p))

    time0 = time.time()

    sl = Solution()
    result = sl.findAnagrams(s, p)

    print("result = %s" %result)

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()


if __name__ == "__main__":
    main()
