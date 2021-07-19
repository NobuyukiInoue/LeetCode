package solution

import (
	"fmt"
	"strings"
	"time"
)

func findCenter(edges [][]int) int {
	// 116ms
	n1, n2 := edges[0][0], edges[0][1]
	if n1 == edges[1][0] || n1 == edges[1][1] {
		return n1
	}
	return n2
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	edges := make([][]int, len(flds))
	for i := 0; i < len(edges); i++ {
		edges[i] = StringToIntArray(flds[i])
	}
	fmt.Printf("edges = %s\n", IntIntArrayToString(edges))

	timeStart := time.Now()

	result := findCenter(edges)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
