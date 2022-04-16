package solution

import (
	"container/heap"
	"fmt"
	"strconv"
	"strings"
	"time"
)

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

func largestInteger(num int) int {
	// 3ms
	odd, even, nums := &IntHeap{}, &IntHeap{}, strconv.Itoa(num)
	heap.Init(odd)
	heap.Init(even)
	for _, n := range nums {
		num := int(n - '0')
		if num%2 == 1 {
			heap.Push(odd, num)
		} else {
			heap.Push(even, num)
		}
	}
	res := 0
	for _, n := range nums {
		if int(n-'0')%2 == 1 {
			res = res*10 + heap.Pop(odd).(int)
		} else {
			res = res*10 + heap.Pop(even).(int)
		}
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)
	num, _ := strconv.Atoi(flds)
	fmt.Printf("num = %d\n", num)

	timeStart := time.Now()

	result := largestInteger(num)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
