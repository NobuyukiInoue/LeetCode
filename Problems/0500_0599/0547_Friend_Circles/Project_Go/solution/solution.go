package solution

import (
	"fmt"
	"strings"
	"time"
)

func findCircleNum(M [][]int) int {
	// 20ms
	visited := make([]int, len(M))
	count := 0
	for i := 0; i < len(M); i++ {
		if visited[i] == 0 {
			dfs(M, visited, i)
			count++
		}
	}
	return count
}

func dfs(M [][]int, visited []int, i int) {
	for j := 0; j < len(M); j++ {
		if M[i][j] == 1 && visited[j] == 0 {
			visited[j] = 1
			dfs(M, visited, j)
		}
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	flds := strings.Replace(temp, "]]", "", -1)

	str_M := strings.Split(flds, "],[")
	M := make([][]int, len(str_M))
	for i := 0; i < len(str_M); i++ {
		M[i] = StringToIntArray(str_M[i])
	}
	fmt.Printf("M = %s\n", IntIntArrayToGridString(M))

	timeStart := time.Now()

	result := findCircleNum(M)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
