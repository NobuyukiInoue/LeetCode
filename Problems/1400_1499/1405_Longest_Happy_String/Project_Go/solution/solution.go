package solution

import (
	"container/heap"
	"fmt"
	"strconv"
	"strings"
	"time"
)

type pair struct {
	c   byte
	cnt int
}

type maxHeap []pair

func (m maxHeap) Len() int {
	return len(m)
}

func (m maxHeap) Less(a, b int) bool {
	return m[a].cnt > m[b].cnt
}

func (m maxHeap) Swap(a, b int) {
	m[a], m[b] = m[b], m[a]
}

func (m *maxHeap) Push(x interface{}) {
	*m = append(*m, x.(pair))
}

func (m *maxHeap) Pop() interface{} {
	n := len(*m)
	x := (*m)[n-1]
	*m = (*m)[0 : n-1]
	return x
}

func longestDiverseString(a int, b int, c int) string {
	m := &maxHeap{}
	heap.Init(m)
	if a > 0 {
		heap.Push(m, pair{'a', a})
	}
	if b > 0 {
		heap.Push(m, pair{'b', b})
	}
	if c > 0 {
		heap.Push(m, pair{'c', c})
	}
	sb := []byte{}
	for m.Len() > 0 {
		first := heap.Pop(m).(pair)
		if len(sb) > 0 && sb[len(sb)-1] == first.c {
			if m.Len() == 0 {
				return string(sb)
			}
			second := heap.Pop(m).(pair)

			sb = append(sb, second.c)
			second.cnt--
			if second.cnt != 0 {
				heap.Push(m, second)
			}
			heap.Push(m, first)
		} else {
			limit := myMin(2, first.cnt)
			for i := 0; i < limit; i++ {
				first.cnt--
				sb = append(sb, first.c)
			}
			if first.cnt != 0 {
				heap.Push(m, first)
			}
		}
	}
	return string(sb)
}

func myMin(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	a, _ := strconv.Atoi(flds[0])
	b, _ := strconv.Atoi(flds[1])
	c, _ := strconv.Atoi(flds[2])
	fmt.Printf("a = %d, b = %d, c = %d\n", a, b, c)

	timeStart := time.Now()

	result := longestDiverseString(a, b, c)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
