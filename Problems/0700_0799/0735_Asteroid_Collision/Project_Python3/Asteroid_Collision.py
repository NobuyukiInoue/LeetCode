# coding: utf-8

import collections
import os
import sys
import time

class Solution:
#   def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    def asteroidCollision(self, asteroids):
        # 104ms
        stack = []
        for asteroid in asteroids:
            if asteroid < 0:
                while asteroid < 0 and stack and stack[-1] > 0:
                    if stack[-1] > abs(asteroid):
                        asteroid = 0
                    elif stack[-1] == abs(asteroid):
                        stack.pop()
                        asteroid = 0
                    else:
                        stack.pop()
                if asteroid:
                    stack.append(asteroid)
            else:
                stack.append(asteroid)
        return stack

    def asteroidCollision2(self, asteroids):
        # 2860ms
        req_CollisionCheck = True
        while req_CollisionCheck:
            req_CollisionCheck = False
            if len(asteroids) <= 0:
                break
            if asteroids[0] >= 0:
                direction = 1
            else:
                direction = -1
            for i in range(len(asteroids) - 1):
                if asteroids[i]*asteroids[i + 1] < 0:
                    if direction == 1:
                        if abs(asteroids[i]) == abs(asteroids[i + 1]):
                            asteroids = asteroids[:i] + asteroids[i+2:]
                        elif abs(asteroids[i]) > abs(asteroids[i + 1]):
                            asteroids = asteroids[:i+1] + asteroids[i+2:]
                        else:
                            asteroids = asteroids[:i] + asteroids[i+1:]
                        req_CollisionCheck = True
                        break
                    else:
                        direction = -direction
        return asteroids

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()

    asteroids = [int(n) for n in flds.split(",")]
    print("arr = {0}".format(asteroids))

    sl = Solution()
    time0 = time.time()
    result = sl.asteroidCollision(asteroids)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
