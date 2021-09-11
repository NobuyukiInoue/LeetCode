package solution

import (
	"fmt"
	"strings"
	"time"
)

func eventualSafeNodes(graph [][]int) []int {
	// 129ms
	n := len(graph)
	visited := make([]bool, n)
	recStack := make([]bool, n)
	nodeInCycle := make([]bool, n)
	res := make([]int, 0)
	for i := 0; i < n; i++ {
		if !visited[i] {
			checkIfNodeIsSafe(graph, nodeInCycle, visited, recStack, i, n)
		}
	}
	for i := 0; i < n; i++ {
		if !nodeInCycle[i] {
			res = append(res, i)
		}
	}
	return res
}

func checkIfNodeIsSafe(graph [][]int, nodeInCycle []bool, visited []bool, recStack []bool, i int, n int) bool {
	if recStack[i] {
		nodeInCycle[i] = true
		return false
	}

	if visited[i] {
		return true
	}

	visited[i] = true
	recStack[i] = true

	for _, j := range graph[i] {
		if !checkIfNodeIsSafe(graph, nodeInCycle, visited, recStack, j, n) {
			nodeInCycle[i] = true
			return false
		}
	}
	nodeInCycle[i] = false
	recStack[i] = false
	return true
}

/*
var memo []bool

func eventualSafeNodes(graph [][]int) []int {
	memo = make([]bool, len(graph))

	result := make([]int, 0)
	for i := 0; i < len(graph); i++ {
		if canJump(graph, i) {
			result = append(result, i)
		}
	}

	return result
}

func canJump(graph [][]int, node int) bool {
	if memo[node] != nil {
		return memo[node]
	}

	memo[node] = false
	for _, child := range graph[node] {
		if !canJump(graph, child) {
			return false
		}
	}
	memo[node] = true

	return memo[node]
}
*/

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	flds := strings.Replace(temp, "]]", "", -1)

	str_graph := strings.Split(flds, "],[")
	graph := make([][]int, len(str_graph))
	for i := 0; i < len(str_graph); i++ {
		if str_graph[i] != "" {
			graph[i] = StringToIntArray(str_graph[i])
		} else {
			graph[i] = make([]int, 0)
		}
	}
	fmt.Printf("graph = %s\n", IntIntArrayToString(graph))

	timeStart := time.Now()

	result := eventualSafeNodes(graph)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
