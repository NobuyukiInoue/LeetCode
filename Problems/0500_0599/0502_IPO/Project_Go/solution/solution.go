package solution

import (
	"container/heap"
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

// 188ms
func findMaximizedCapital(k int, w int, profits []int, capital []int) int {
	projects := make([][2]int, len(profits))
	for i := 0; i < len(projects); i++ {
		projects[i] = [2]int{profits[i], capital[i]}
	}
	sort.Slice(projects, func(i, j int) bool {
		return projects[i][1] < projects[j][1]
	})
	var ih = &IntHeap{}
	heap.Init(ih)
	j := 0
	for i := 0; i < k; i++ {
		for j < len(profits) && projects[j][1] <= w {
			heap.Push(ih, projects[j][0])
			j++
		}

		if ih.Len() > 0 {
			w += (heap.Pop(ih)).(int)
		}
	}
	return w
}

type IntHeap []int

func (ih IntHeap) Len() int {
	return len(ih)
}

func (ih IntHeap) Less(i, j int) bool {
	return ih[i] > ih[j]
}

func (ih IntHeap) Swap(i, j int) {
	ih[i], ih[j] = ih[j], ih[i]
}

func (ih *IntHeap) Push(x interface{}) {
	*ih = append(*ih, x.(int))
}

func (ih *IntHeap) Pop() interface{} {
	pre := *ih
	n := len(pre)
	x := pre[n-1]
	*ih = pre[0 : n-1]
	return x
}

/*
func findMaximizedCapital(k int, w int, profits []int, capital []int) int {
	// Time Limite Exceeded.
	mySort(profits, capital)
	pq := make([]int, 0)
	for i := 0; i < k; {
		for i < len(capital) && capital[i] <= w {
			// push
			pq = append(pq, -profits[i])
			i++
		}
		if len(pq) > 0 {
			// pop
			w -= pq[len(pq)-1]
			pq = pq[:len(pq)-1]
		}
	}
	return w
}

func mySort(profits []int, capital []int) {
	for i := 0; i < len(profits)-1; i++ {
		for j := i + 1; j < len(profits); j++ {
			if profits[i] > profits[j] {
				profits[i], profits[j] = profits[j], profits[i]
				capital[i], capital[j] = capital[j], capital[i]
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

	k, _ := strconv.Atoi(flds[0])
	w, _ := strconv.Atoi(flds[1])
	profits := StringToIntArray(flds[2])
	capital := StringToIntArray(flds[3])
	fmt.Printf("k = %d, w = %d, profits = [%s], capital = [%s]\n", k, w, IntArrayToString(profits), IntArrayToString(capital))

	timeStart := time.Now()

	result := findMaximizedCapital(k, w, profits, capital)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
