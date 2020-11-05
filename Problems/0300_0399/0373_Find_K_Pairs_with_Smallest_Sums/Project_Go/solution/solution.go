package solution

import (
	"container/heap"
	"fmt"
	"strconv"
	"strings"
	"time"
)

// 4ms
type Pair struct {
	IdxInNums1 int
	IdxInNums2 int
	Val        int
}

type PairHeap []Pair

func (ph PairHeap) Len() int {
	return len(ph)
}

func (ph PairHeap) Less(i, j int) bool {
	return ph[i].Val < ph[j].Val
}

func (ph PairHeap) Swap(i, j int) {
	ph[i], ph[j] = ph[j], ph[i]
}

func (ph *PairHeap) Push(x interface{}) {
	*ph = append(*ph, x.(Pair))
}

func (ph *PairHeap) Pop() interface{} {
	root := (*ph)[len(*ph)-1]
	*ph = (*ph)[:len(*ph)-1]
	return root
}

func kSmallestPairs(nums1 []int, nums2 []int, k int) [][]int {
	if len(nums1) == 0 || len(nums2) == 0 {
		return nil
	}
	// Init heap
	ph := new(PairHeap)
	heap.Init(ph)
	for i := 0; i < len(nums2); i++ {
		heap.Push(ph, Pair{0, i, nums1[0] + nums2[i]})
	}
	// Generate ohther pairs and get first k smallest paris
	res := make([][]int, 0)
	if k > len(nums1)*len(nums2) {
		k = len(nums1) * len(nums2)
	}
	for i := 0; i < k; i++ {
		pair := heap.Pop(ph).(Pair)
		res = append(res, []int{nums1[pair.IdxInNums1], nums2[pair.IdxInNums2]})
		if pair.IdxInNums1 < len(nums1)-1 {
			heap.Push(ph, Pair{pair.IdxInNums1 + 1, pair.IdxInNums2, nums1[pair.IdxInNums1+1] + nums2[pair.IdxInNums2]})
		}
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	nums1 := StringToIntArray(flds[0])
	nums2 := StringToIntArray(flds[1])
	k, _ := strconv.Atoi(flds[2])
	fmt.Printf("nums1 = [%s], nums2 = [%s], k = %d\n", IntArrayToString(nums1), IntArrayToString(nums2), k)

	timeStart := time.Now()

	result := kSmallestPairs(nums1, nums2, k)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntIntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
