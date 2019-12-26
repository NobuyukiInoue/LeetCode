import collections
import os
import sys
import time

class Solution:
#   def numFriendRequests(self, ages: List[int]) -> int:
    def numFriendRequests(self, ages):
        # 264ms
        cnt = collections.Counter(ages)
        ans, s, sm = 0, 15, 0
        for i in sorted(cnt):
            if i < 15:
                continue
            x = i//2 + 8
            for j in range(s, x):
                sm -= cnt[j]
            s = x
            sm += cnt[i]
            ans += cnt[i]*sm-cnt[i]
        return ans

    def numFriendRequests2(self, ages):
        # 392ms
        def request(a, b):
            return not (b <= 0.5 * a + 7 or b > a or b > 100 and a < 100)
        c = collections.Counter(ages)
        return sum(request(a, b) * c[a] * (c[b] - (a == b)) for a in c for b in c)

    def numFriendRequests_work(self, ages):
        res = 0
        for i in range(len(ages)):
            for j in range(len(ages)):
                if i == j:
                    continue
                if ages[j] <= 0.5*ages[i] + 7:
                    continue
                elif ages[j] > ages[i]:
                    continue
                elif ages[j] > 100 and ages[i] < 100:
                    continue
                res += 1
        return res

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
    flds = temp.replace("\"","").replace("[","").replace("]","").rstrip()

    ages = [int(val) for val in flds.split(",")]
    print("ages = {0}".format(ages))

    time0 = time.time()

    sl = Solution()
    result = sl.numFriendRequests(ages)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
