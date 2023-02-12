package solution

import (
	"container/heap"
	"fmt"
	"math"
	"strconv"
	"strings"
	"time"
)

// 3ms- 7ms

type IntHeap []int

func (h IntHeap) Len() int            { return len(h) }
func (h IntHeap) Less(i, j int) bool  { return h[i] > h[j] }
func (h IntHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *IntHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func pickGifts(gifts []int, k int) int64 {
	pq := &IntHeap{}
	for _, gift := range gifts {
		heap.Push(pq, gift)
	}
	for i := 0; i < k; i++ {
		n := int(math.Sqrt(float64(heap.Pop(pq).(int))))
		pq.Push(n)
	}
	var ans int64 = 0
	for i := 0; i < len(gifts); i++ {
		ans += int64(heap.Pop(pq).(int))
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	gifts := StringToIntArray(flds[0])
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("gifts = [%s], k = %d\n", IntArrayToString(gifts), k)

	timeStart := time.Now()

	result := pickGifts(gifts, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
