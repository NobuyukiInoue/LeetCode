package solution

import (
	"container/heap"
	"fmt"
	"strings"
	"time"
)

// 4ms

type Item struct {
	value int
	freq  int
}

type Pqueue []*Item

func (q Pqueue) Len() int { return len(q) }

func (q *Pqueue) Push(val interface{}) {
	item := val.(*Item)
	*q = append(*q, item)
}

func (q *Pqueue) Pop() interface{} {
	old := *q
	n := len(old)
	item := old[n-1]
	old[n-1] = nil
	*q = old[0 : n-1]
	return item
}

func (q Pqueue) Swap(i, j int) {
	q[i], q[j] = q[j], q[i]
}

func (q Pqueue) Less(i, j int) bool {
	if q[i].freq == q[j].freq {
		return q[i].value > q[j].value
	}
	return q[i].freq < q[j].freq
}

func frequencySort(nums []int) []int {
	l := len(nums)
	result := []int{}

	if l == 0 {
		return result
	}

	if l == 1 {
		return nums
	}

	freqMap := make(map[int]int)

	for i := 0; i < l; i++ {
		v, ok := freqMap[nums[i]]
		if ok {
			freqMap[nums[i]] = v + 1
		} else {
			freqMap[nums[i]] = 1
		}
	}

	pq := &Pqueue{}

	for key, value := range freqMap {
		heap.Push(pq, &Item{
			value: key,
			freq:  value,
		})
	}

	for len(*pq) > 0 {
		popped := heap.Pop(pq)

		//	fmt.Println(popped.(*Item))

		for i := 0; i < popped.(*Item).freq; i++ {
			result = append(result, popped.(*Item).value)
		}
	}

	return result
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	nums := StringToIntArray(flds)
	fmt.Printf("nums = [%s]\n", IntArrayToString(nums))

	timeStart := time.Now()

	result := frequencySort(nums)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
