package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func findMinHeightTrees(n int, edges [][]int) []int {
	// 56ms
	if n <= 1 {
		return []int{0}
	}

	adjacentMap := make(map[int]map[int]bool)
	for i := 0; i < n; i++ {
		adjacentMap[i] = make(map[int]bool)
	}
	for _, edge := range edges {
		a, b := edge[0], edge[1]
		adjacentMap[a][b] = true
		adjacentMap[b][a] = true
	}

	queue := []int{}
	for i := 0; i < n; i++ {
		if len(adjacentMap[i]) == 1 {
			queue = append(queue, i)
		}
	}

	for len(queue) > 0 {
		if len(queue) == 2 {
			a, b := queue[0], queue[1]
			if adjacentMap[a][b] && adjacentMap[b][a] {
				return queue
			}
		}

		next := []int{}
		for _, node := range queue {
			for neighbor := range adjacentMap[node] {
				if len(adjacentMap[neighbor]) == 1 {
					return []int{neighbor}
				}

				delete(adjacentMap[neighbor], node)
				delete(adjacentMap[node], neighbor)
				if len(adjacentMap[neighbor]) == 1 {
					next = append(next, neighbor)
				}
			}
		}

		queue = next
	}

	return []int{}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	flds := strings.Split(temp, "],[[")

	flds[0] = strings.Replace(flds[0], "[", "", -1)
	n, _ := strconv.Atoi(flds[0])
	fmt.Printf("n = %d\n", n)

	flds[1] = strings.Replace(flds[1], "]]]", "", -1)
	dataStr := strings.Split(flds[1], "],[")

	var edges [][]int
	if len(dataStr) > 0 {
		edges = make([][]int, len(dataStr))
		for i := 0; i < len(edges); i++ {
			edges[i] = StringToIntArray(dataStr[i])
		}
	} else {
		edges = make([][]int, 0)
	}
	fmt.Printf("edges = %s\n", IntIntArrayToGridString(edges))

	timeStart := time.Now()

	result := findMinHeightTrees(n, edges)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
