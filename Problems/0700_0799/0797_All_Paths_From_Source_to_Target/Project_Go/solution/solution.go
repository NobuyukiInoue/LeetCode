package solution

import (
	"fmt"
	"strings"
	"time"
)

func allPathsSourceTarget(graph [][]int) [][]int {
	// 4ms
	ans, path := [][]int{}, []int{}
	dfs(&graph, &ans, &path, 0)
	return ans
}

func dfs(graph, ans *[][]int, path *[]int, i int) {
	*path = append(*path, i)
	if i == len(*graph)-1 {
		tmp := make([]int, len(*path))
		copy(tmp, *path)
		*ans = append(*ans, tmp)
	} else {
		for _, v := range (*graph)[i] {
			dfs(graph, ans, path, v)
		}
	}
	*path = (*path)[:len(*path)-1]
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	//	graph := make([][]int, len(flds)+1)
	graph := make([][]int, len(flds))
	for i := 0; i < len(flds); i++ {
		graph[i] = StringToIntArray(flds[i])
	}
	fmt.Printf("graph = %s\n", IntIntArrayToString(graph))

	timeStart := time.Now()

	result := allPathsSourceTarget(graph)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntIntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
