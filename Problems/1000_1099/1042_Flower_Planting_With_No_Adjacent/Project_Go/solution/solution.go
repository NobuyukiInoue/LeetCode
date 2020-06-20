package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func gardenNoAdj(N int, paths [][]int) []int {
	connects := make([][]int, N)
	for _, p := range paths {
		i, j := p[0]-1, p[1]-1 // i,j = x-1, y-1
		connects[i] = append(connects[i], j)
		connects[j] = append(connects[j], i)
	}
	res := make([]int, N)
	for i := 0; i < N; i++ {
		isUsed := [5]bool{}
		for _, j := range connects[i] {
			isUsed[res[j]] = true
		}
		for color := 1; color <= 4; color++ {
			if !isUsed[color] {
				res[i] = color
				break
			}
		}
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "]]]", "", -1)
	flds := strings.Split(temp, "],[[")

	N, _ := strconv.Atoi(strings.Replace(flds[0], "[[", "", -1))
	data := strings.Split(flds[1], "],[")

	paths := make([][]int, len(data))
	for i := 0; i < len(data); i++ {
		paths[i] = StringToIntArray(data[i])
	}

	fmt.Printf("paths = %s\n", IntIntArrayToString(paths))

	timeStart := time.Now()

	result := gardenNoAdj(N, paths)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
