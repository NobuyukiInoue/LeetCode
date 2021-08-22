package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func validPath(n int, edges [][]int, start int, end int) bool {
	// 416ms
	seen := make([][]int, n)
	for _, edge := range edges {
		seen[edge[0]] = append(seen[edge[0]], edge[1])
		seen[edge[1]] = append(seen[edge[1]], edge[0])
	}
	visited := map[int]struct{}{}
	none := struct{}{}
	que := []int{start}
	for len(que) > 0 {
		sz := len(que)
		for i := 0; i < sz; i++ {
			item := que[0]
			if item == end {
				return true
			}
			if _, ok := visited[item]; !ok {
				que = append(que, seen[item]...)
				visited[item] = none
			}
		}
		que = que[1:]
	}
	return false
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	flds := strings.Split(temp, "],[[")
	n, _ := strconv.Atoi(strings.Replace(flds[0], "[", "", -1))

	flds1 := strings.Split(flds[1], "]],[")

	var edges [][]int

	if len(flds1[0]) == 0 {
		edges = make([][]int, 0)
	} else {
		flds10 := strings.Split(flds1[0], "],[")
		edges = make([][]int, len(flds10))
		for i := 0; i < len(flds10); i++ {
			edges[i] = StringToIntArray(flds10[i])
		}
	}
	flds2 := strings.Split(strings.Replace(flds1[1], "]]", "", -1), "],[")
	start, _ := strconv.Atoi(flds2[0])
	end, _ := strconv.Atoi(flds2[1])
	fmt.Printf("n = %d, edges = %s, start = %d, end = %d\n", n, IntIntArrayToString(edges), start, end)

	timeStart := time.Now()

	result := validPath(n, edges, start, end)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
