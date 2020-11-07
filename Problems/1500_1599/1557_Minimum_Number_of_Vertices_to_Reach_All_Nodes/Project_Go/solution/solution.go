package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func findSmallestSetOfVertices(n int, edges [][]int) []int {
    // 180ms
    visited := make([]bool, n)
    for i := 0; i < len(edges); i++ {
        visited[edges[i][1]] = true
    }

    ans := make([]int, 0)
    for j := 0; j < n; j++ {
        if !visited[j] {
            ans = append(ans, j)
        }
    }

    return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	flds := strings.Split(temp, "],[[")

	n, _ := strconv.Atoi(strings.Replace(flds[0], "[[", "", -1))
	fmt.Printf("n = %d\n", n)

	str_edges := strings.Split(strings.Replace(flds[1], "]]]", "", -1), "],[")
	edges := make([][]int, len(str_edges))
	for i := 0; i < len(str_edges); i++ {
		edges[i] = StringToIntArray(str_edges[i])
	}
	fmt.Printf("edges = %s\n", IntIntArrayToString(edges))

	timeStart := time.Now()

	result := findSmallestSetOfVertices(n, edges)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
