package solution

import (
	"fmt"
	"strings"
	"time"
)

func countStudents(students []int, sandwiches []int) int {
	// 0ms
	cnt := map[int]int{}
	for _, n := range students {
		cnt[n]++
	}

	n := len(students)
	k := 0

	if cnt[sandwiches[k]] == 0 {
		return n
	}

	for k < n && cnt[sandwiches[k]] > 0 {
		cnt[sandwiches[k]]--
		k++
	}

	return n - k
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	students := StringToIntArray(flds[0])
	sandwiches := StringToIntArray(flds[1])
	fmt.Printf("students   = %s\n", IntArrayToString(students))
	fmt.Printf("sandwiches = %s\n", IntArrayToString(sandwiches))

	timeStart := time.Now()

	result := countStudents(students, sandwiches)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
