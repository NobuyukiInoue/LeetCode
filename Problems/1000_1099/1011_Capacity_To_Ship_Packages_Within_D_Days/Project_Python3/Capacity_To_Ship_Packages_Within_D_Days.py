import os
import sys
import time

class Solution0:
#   def shipWithinDays(self, weights: List[int], D: int) -> int:
    def shipWithinDays(self, weights, D):
        # 388ms
        def canShip(capacity: int) -> bool:
            nonlocal D
            count = 1
            loaded = 0 
            for w in weights:
                if loaded + w <= capacity:
                    loaded += w
                else:
                    count += 1
                    loaded = w
            return count <= D
        
        maxWeight = max(weights)
        lo = sum(weights) // D
        hi = maxWeight * (len(weights) // D + 1)
        while lo < hi:
            mid = (lo + hi) // 2
            if mid < maxWeight or not canShip(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo

class Solution:
#   def shipWithinDays(self, weights: List[int], D: int) -> int:
    def shipWithinDays(self, weights, D):
        # Time Limit Exceeded(10.48ms)
        sums = [0 for i in range(D)]
        return self.helper(weights, D, sums)

    def helper(self, sub_weights, d, sums):
        if d == 1:
            sums[len(sums) - d] = sum(sub_weights)
            return self.max_total_sums(sums)
        else:
            min_total = sys.maxsize
            for i in range(1, len(sub_weights) - d + 2):
                sums[len(sums) - d] = sum(sub_weights[:i])
                total = self.helper(sub_weights[i:], d - 1, sums.copy())
                if total < min_total:
                    min_total = total
            return min_total

    def max_total_sums(self, sums):
        max_total = 0
        for data in sums:
            if data > max_total:
                max_total = data
        return max_total

class Solution2:
#   def shipWithinDays(self, weights: List[int], D: int) -> int:
    def shipWithinDays(self, weights, D):
        # Time Limit Exceeded(13.72ms)
        items = [None for i in range(D)]
        sums = [0 for i in range(D)]
        return self.helper(weights, D, items, sums)

    def helper(self, sub_weights, d, items, sums):
        if d == 1:
            items[len(items) - d] = sub_weights
            sums[len(items) - d] = sum(sub_weights)
            return self.max_total_items(sums)
        else:
            min_total = sys.maxsize
            for i in range(1, len(sub_weights) - d + 2):
                items[len(items) - d] = sub_weights[:i]
                sums[len(items) - d] = sum(sub_weights[:i])
                total = self.helper(sub_weights[i:], d - 1, items.copy(), sums.copy())
                if total < min_total:
                    min_total = total
            return min_total

    def max_total_items(self, sums):
        max_total = 0
        for data in sums:
            if data > max_total:
                max_total = data
        return max_total

class Solution3:
#   def shipWithinDays(self, weights: List[int], D: int) -> int:
    def shipWithinDays(self, weights, D):
        # Time Limit Exceeded(18.34ms)
        items = [[None, 0] for i in range(D)]
        return self.helper(weights, D, items)

    def helper(self, sub_weights, d, items):
        if d == 1:
            items[len(items) - d][0] = sub_weights
            items[len(items) - d][1] = sum(sub_weights)
            return self.max_total_items(items)
        else:
            min_total = sys.maxsize
            for i in range(1, len(sub_weights) - d + 2):
                items[len(items) - d][0] = sub_weights[:i]
                items[len(items) - d][1] = sum(sub_weights[:i])
                total = self.helper(sub_weights[i:], d - 1, items.copy())
                if total < min_total:
                    min_total = total
            return min_total

    def max_total_items(self, items):
        max_total = 0
        for data in items:
            if data[1] > max_total:
                max_total = data[1]
        return max_total

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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    weights = [int(val) for val in str_args[0].split(",")]
    D = int(str_args[1])
    print("weights = {0}, D = {1}".format(weights, D))

    sl = Solution()
    time0 = time.time()
    result = sl.shipWithinDays(weights, D)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
