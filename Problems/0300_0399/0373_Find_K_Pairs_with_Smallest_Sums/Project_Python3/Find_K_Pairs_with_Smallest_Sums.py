# coding: utf-8

import heapq
import os
import sys
import time

class Solution:
#   def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    def kSmallestPairs(self, nums1, nums2, k):
        # 48ms
        if not nums1 or not nums2:
            return []
        n, res, cnt, heap = len(nums2), [], 0, [(nums1[i] + nums2[0], i, 0) for i in range(len(nums1))]
        while heap and cnt < k:
            cnt += 1
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < n:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return res

    def kSmallestPairs2(self, nums1, nums2, k):
        # 56ms
        heap = []
        for n1 in nums1:
            for n2 in nums2:
                if len(heap) < k: heapq.heappush(heap, (-n1 - n2, [n1, n2]))
                else:
                    if heap and -heap[0][0] > n1 + n2:
                        heapq.heappop(heap)
                        heapq.heappush(heap, (-n1 - n2, [n1, n2]))
                    else: break
        return [heapq.heappop(heap)[1] for _ in range(k) if heap]

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
    nums1 = [int(n) for n in flds[0].split(",")]
    nums2 = [int(n) for n in flds[1].split(",")]
    k = int(flds[2])

    print("nums1 = {0}, nums2 = {1}, k = {2}".format(nums1, nums2, k))

    sl = Solution()
    time0 = time.time()

    result = sl.kSmallestPairs(nums1, nums2, k)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
