# coding: utf-8

import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def minNumberOfHours2(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        # 41ms - 59ms
        enery_required = 0
        total_energy = sum(energy)
        if total_energy >= initialEnergy:
            enery_required = total_energy - initialEnergy + 1
        exp_required = 0
        for exp in experience:
            training_exp = 0
            if initialExperience <= exp:
                training_exp = exp - initialExperience + 1
                exp_required += training_exp
            initialExperience += exp + training_exp
        return enery_required + exp_required

    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        # 62ms - 98m
        en, ex, add_en, add_ex = 0, 0, 0, 0
        for ener, exp in zip(energy, experience):
            if ener >= en:
                add_en += (ener - en + 1)
                en += (ener - en + 1)
            if exp >= ex:
                add_ex += (exp - ex + 1)
                ex += (exp - ex + 1)
            en -= ener
            ex += exp
        return max(0, (add_en - initialEnergy)) + max(0, (add_ex - initialExperience))

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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    initialEnergy, initialExperience = int(flds[0]), int(flds[1])
    energy = [int(n) for n in flds[2].split(",")]
    experience = [int(n) for n in flds[3].split(",")]

    print("initialEnergy = {0:d}, initialExperience = {1:d}, energy = {2}, experience = {3}".format(initialEnergy, initialExperience, energy, experience))

    sl = Solution()
    time0 = time.time()

    result = sl.minNumberOfHours(initialEnergy, initialExperience, energy, experience)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
