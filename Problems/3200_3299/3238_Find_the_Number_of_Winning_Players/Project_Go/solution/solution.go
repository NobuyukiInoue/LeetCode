package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func winningPlayerCount(n int, pick [][]int) int {
	// 7ms - 21ms
	balls := make([][]int, n)
	for i := 0; i < n; i++ {
		balls[i] = make([]int, 11)
	}
	winner := make([]int, n)
	for _, p := range pick {
		balls[p[0]][p[1]]++
		if balls[p[0]][p[1]] == p[0]+1 {
			winner[p[0]] = 1
		}
	}
	ans := 0
	for _, val := range winner {
		if val == 1 {
			ans++
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "]]]", "", -1)
	flds := strings.Split(temp, "],[[")
	flds1 := strings.Split(flds[1], "],[")
	n, _ := strconv.Atoi(strings.Replace(flds[0], "[[", "", -1))

	pick := make([][]int, len(flds1))
	for i, _ := range flds1 {
		pick[i] = StringToIntArray(flds1[i])
	}

	fmt.Printf("n = %d, pick = %s\n", n, IntIntArrayToString(pick))

	timeStart := time.Now()

	result := winningPlayerCount(n, pick)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
