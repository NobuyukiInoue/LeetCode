package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func maximalNetworkRank(n int, roads [][]int) int {
	// 29ms
	connections := make([]int, n)
	graph := make([][]bool, n)
	for i := 0; i < n; i++ {
		graph[i] = make([]bool, n)
	}
	for _, cities := range roads {
		connections[cities[0]]++
		connections[cities[1]]++
		graph[cities[0]][cities[1]], graph[cities[1]][cities[0]] = true, true
	}
	maxRank := 0
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			rank := connections[i] + connections[j]
			if graph[i][j] {
				rank--
			}
			maxRank = myMax(rank, maxRank)
		}
	}
	return maxRank
}

func myMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "]]]", "", -1)
	flds := strings.Split(temp, "],[[")
	flds1 := strings.Split(flds[1], "],[")
	n, _ := strconv.Atoi(strings.Replace(flds[0], "[[", "", -1))

	roads := make([][]int, len(flds1))
	for i, _ := range flds1 {
		roads[i] = StringToIntArray(flds1[i])
	}

	fmt.Printf("n = %d, roads = %s\n", n, IntIntArrayToString(roads))

	timeStart := time.Now()

	result := maximalNetworkRank(n, roads)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
