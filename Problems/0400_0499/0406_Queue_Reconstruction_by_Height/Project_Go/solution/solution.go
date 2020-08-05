package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func reconstructQueue(people [][]int) [][]int {
	// 8ms
	sort.Slice(people, func(i, j int) bool {
		if people[i][0] == people[j][0] {
			return people[i][1] > people[j][1]
		}
		return people[i][0] < people[j][0]
	})
	indexes := make([]int, len(people))
	for i := range indexes {
		indexes[i] = i
	}
	queued := make([][]int, len(people))
	for _, v := range people {
		queued[indexes[v[1]]] = v
		indexes = append(indexes[:v[1]], indexes[v[1]+1:]...)
	}
	return queued
}

func myMin(a int, b int) int {
	if a < b {
		return a
	}

	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	flds := strings.Replace(temp, "]]", "", -1)

	peopleStr := strings.Split(flds, "],[")
	people := make([][]int, len(peopleStr))
	for i := 0; i < len(peopleStr); i++ {
		people[i] = StringToIntArray(peopleStr[i])
	}
	fmt.Printf("people = %s\n", IntIntArrayToGridString(people))

	timeStart := time.Now()

	result := reconstructQueue(people)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntIntArrayToGridString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
