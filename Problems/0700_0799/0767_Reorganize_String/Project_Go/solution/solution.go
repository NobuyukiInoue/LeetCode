package solution

import (
	"container/heap"
	"fmt"
	"strings"
	"time"
)

// 0ms
type item struct {
	val   rune
	count int
}

type pqueue []item

func (pq pqueue) Less(i, j int) bool {
	return pq[i].count > pq[j].count
}

func (pq pqueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
}

func (pq pqueue) Len() int {
	return len(pq)
}

func (pq *pqueue) Push(x interface{}) {
	*pq = append(*pq, x.(item))
}

func (pq *pqueue) Pop() interface{} {
	res := (*pq)[pq.Len()-1]
	*pq = (*pq)[:pq.Len()-1]
	return res
}

func reorganizeString(S string) string {
	dict := make(map[rune]int)
	for _, c := range S {
		dict[c]++
	}

	pq := &pqueue{}
	heap.Init(pq)

	for k, v := range dict {
		heap.Push(pq, item{k, v})
	}

	res := make([]rune, 0)
	for pq.Len() > 0 {
		item1 := heap.Pop(pq).(item)
		if pq.Len() == 0 {
			if len(res) > 0 && res[len(res)-1] == item1.val || item1.count > 1 {
				return ""
			}
			res = append(res, item1.val)
			break
		}

		item2 := heap.Pop(pq).(item)
		res = append(res, item1.val)
		res = append(res, item2.val)

		if item1.count > 1 {
			heap.Push(pq, item{item1.val, item1.count - 1})
		}

		if item2.count > 1 {
			heap.Push(pq, item{item2.val, item2.count - 1})
		}
	}

	return string(res)
}

/*
func reorganizeString(s string) string {
	counts := make([]int, 26)
	for _, ch := range s {
		counts[ch-'a'] += 1
	}

	limit := (len(s) + 1) / 2
	pq := make([][]int, 0)
	for i := 0; i < len(counts); i++ {
		if counts[i] > limit {
			return ""
		}
		if counts[i] > 0 {
			// Bad!! no priority sort.
			pq = append(pq, []int{counts[i], 'a' + i})
		}
	}

	res := ""
	for len(pq) > 0 {
		cur := pq[0]
		pq = pq[1:]
		if len(res) == 0 || res[len(res)-1] != byte(cur[1]) {
			res += string(rune(cur[1]))
			if cur[0] > 1 {
				cur[0] -= 1
				pq = append(pq, cur)
			}
		} else {
			p := pq[0]
			pq = pq[1:]
			res += string(rune(p[1]))
			if p[0] > 1 {
				p[0] -= 1
				pq = append(pq, p)
			}
			pq = append(pq, cur)
		}
	}
	return res
}
*/

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := reorganizeString(s)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
