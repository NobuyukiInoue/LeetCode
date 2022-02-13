package solution

import (
	"container/heap"
	"fmt"
	"strings"
	"time"
)

func eatenApples(apples []int, days []int) int {
	// 132ms
	apple_heap := &minheap{}
	day, res := 0, 0
	lastday := len(apples)

	for day < lastday {
		if apples[day] > 0 {
			heap.Push(apple_heap, [2]int{day + days[day], apples[day]})
		}
		if apple_heap.Len() > 0 && (*apple_heap)[0][0] > day {
			res++
			(*apple_heap)[0][1]--
			if (*apple_heap)[0][1] == 0 {
				heap.Pop(apple_heap)
			}
		}
		day++

		for apple_heap.Len() > 0 && (*apple_heap)[0][0] <= day {
			heap.Pop(apple_heap)
		}
	}

	for apple_heap.Len() > 0 {
		temp := heap.Pop(apple_heap).([2]int)
		expire, counts := temp[0], temp[1]
		if day < expire {
			jump_to := myMin(expire, day+counts)
			res += jump_to - day
			day = jump_to
		}
	}
	return res
}

func eatenApples2(apples []int, days []int) int {
	// 194ms
	apple_heap := &minheap{}
	res := 0
	i := 0
	for apple_heap.Len() > 0 || i < len(apples) {
		if i < len(apples) && apples[i] != 0 {
			heap.Push(apple_heap, [2]int{i + days[i] - 1, apples[i]})
		}
		for apple_heap.Len() > 0 {
			a := heap.Pop(apple_heap).([2]int)
			if a[0] >= i {
				res++
				a[1]--
				if a[1] != 0 {
					heap.Push(apple_heap, a)
				}
				break
			}
		}
		i++
	}
	return res
}

func myMin(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

type minheap [][2]int

func (h minheap) Len() int {
	return len(h)
}

func (h minheap) Less(i int, j int) bool {
	return h[i][0] < h[j][0]
}

func (h minheap) Swap(i int, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *minheap) Push(a interface{}) {
	*h = append(*h, a.([2]int))
}

func (h *minheap) Pop() interface{} {
	l := len(*h)
	res := (*h)[l-1]
	*h = (*h)[:l-1]
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	apples := StringToIntArray(flds[0])
	days := StringToIntArray(flds[1])
	fmt.Printf("apples = [%s], days = [%s]\n", IntArrayToString(apples), IntArrayToString(days))

	timeStart := time.Now()

	result := eatenApples(apples, days)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
