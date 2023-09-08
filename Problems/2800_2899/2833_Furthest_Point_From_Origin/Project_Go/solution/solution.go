package solution

import (
	"fmt"
	"strings"
	"time"
)

func furthestDistanceFromOrigin(moves string) int {
	// 0ms
	l, r, m := 0, 0, 0
	for _, move := range moves {
		if move == 'L' {
			l++
		} else if move == 'R' {
			r++
		} else {
			m++
		}
	}
	if l >= r {
		return l - r + m
	}
	return r - l + m
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	moves := strings.Replace(temp, "]", "", -1)
	fmt.Printf("moves = \"%s\"\n", moves)

	timeStart := time.Now()

	result := furthestDistanceFromOrigin(moves)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
