package solution

import (
	"container/heap"
	"fmt"
	"strconv"
	"strings"
	"time"
)

func largestValsFromLabels(values []int, labels []int, num_wanted int, use_limit int) int {
	// 24ms - 34ms
	hh := &IntHeapLabelHeap{}
	m := make(map[int]*IntHeap)
	for i := 0; i < len(values); i++ {
		if m[labels[i]] == nil {
			m[labels[i]] = &IntHeap{}
		}
		heap.Push(m[labels[i]], values[i])
	}
	for label, h := range m {
		heap.Push(hh, IntHeapLabel{h, label})
	}
	used := make(map[int]int)
	sum := 0
	for i := 0; i < num_wanted && hh.Len() != 0; i++ {
		h := heap.Pop(hh).(IntHeapLabel)
		sum += heap.Pop(h.nums).(int)
		used[h.label]++
		if h.nums.Len() != 0 && used[h.label] < use_limit {
			heap.Push(hh, h)
		}
	}
	return sum
}

// max-heap
type IntHeap []int

func (h IntHeap) Less(i, j int) bool  { return h[i] > h[j] }
func (h IntHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h IntHeap) Len() int            { return len(h) }
func (h *IntHeap) Push(x interface{}) { *h = append(*h, x.(int)) } // add x as element Len()
func (h *IntHeap) Pop() interface{} { // remove and return element Len() - 1.
	x := (*h)[len(*h)-1] // Note: (*h)[i]
	*h = (*h)[:len(*h)-1]
	return x
}

type IntHeapLabel struct {
	nums  *IntHeap
	label int
}

// max-heap
type IntHeapLabelHeap []IntHeapLabel

func (h IntHeapLabelHeap) Less(i, j int) bool  { return (*(h[i].nums))[0] > (*(h[j].nums))[0] }
func (h IntHeapLabelHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h IntHeapLabelHeap) Len() int            { return len(h) }
func (h *IntHeapLabelHeap) Push(x interface{}) { *h = append(*h, x.(IntHeapLabel)) } // add x as element Len()
func (h *IntHeapLabelHeap) Pop() interface{} { // remove and return element Len() - 1.
	x := (*h)[len(*h)-1] // Note: (*h)[i]
	*h = (*h)[:len(*h)-1]
	return x
}

/*
func largestValsFromLabels(values []int, labels []int, numWanted int, useLimit int) int {
	// 935ms - 987ms
	n := len(values)
	hash := make([][]int, n)
	for i := 0; i < n; i++ {
		hash[i] = []int{values[i], labels[i]}
	}
	var cnt [20001]int
	ans := 0
	sort_array_by_val(&hash)
	for _, h := range hash {
		value, label := h[0], h[1]
		cnt[label]++
		if cnt[label] <= useLimit {
			ans += value
			numWanted--
			if numWanted == 0 {
				break
			}
		}
	}
	return ans
}

func sort_array_by_val(arr *[][]int) {
	n := len(*arr)
	for i := 0; i < n; i++ {
		for j := n - 1; j > i; j-- {
			if (*arr)[j-1][0] < (*arr)[j][0] {
				(*arr)[j-1], (*arr)[j] = (*arr)[j], (*arr)[j-1]
			}
		}
	}
}
*/

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	values := StringToIntArray(flds[0])
	labels := StringToIntArray(flds[1])
	numWanted, _ := strconv.Atoi(flds[2])
	useLimit, _ := strconv.Atoi(flds[3])
	fmt.Printf("values = [%s], labels = [%s], numWanted = %d, useLimit = %d\n", IntArrayToString(values), IntArrayToString(labels), numWanted, useLimit)

	timeStart := time.Now()

	result := largestValsFromLabels(values, labels, numWanted, useLimit)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
