package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func minimumBoxes(apple []int, capacity []int) int {
	// 0ms
	sort.Sort(sort.IntSlice(capacity))
	total := 0
	for _, a := range apple {
		total += a
	}
	m, t_cap := len(capacity), 0
	for i := 0; i < m; i++ {
		if t_cap >= total {
			return i
		}
		t_cap += capacity[m-1-i]
	}
	return m
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	apple := StringToIntArray(flds[0])
	capacity := StringToIntArray(flds[1])
	fmt.Printf("apple = %s, capacity = %s\n", IntArrayToString(apple), IntArrayToString(capacity))

	timeStart := time.Now()

	result := minimumBoxes(apple, capacity)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
