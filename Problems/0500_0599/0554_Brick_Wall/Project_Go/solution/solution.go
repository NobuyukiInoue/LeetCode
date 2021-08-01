package solution

import (
	"fmt"
	"strings"
	"time"
)

func leastBricks(wall [][]int) int {
	// 24ms
	count_map := map[int]int{}
	for _, row := range wall {
		pos := 0
		for i := 0; i < len(row)-1; i++ {
			pos += row[i]
			count_map[pos] += 1
		}
	}
	max_pos := 0
	for _, v := range count_map {
		max_pos = myMax(max_pos, v)
	}
	return len(wall) - max_pos
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	wall := make([][]int, len(flds))
	for i := 0; i < len(flds); i++ {
		wall[i] = StringToIntArray(flds[i])
	}
	fmt.Printf("wall = %s\n", IntIntArrayToString(wall))

	timeStart := time.Now()

	result := leastBricks(wall)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
