package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func judgeCircle(moves string) bool {
	x, y := 0, 0
	for _, ch := range moves {
		switch ch {
			case 'U':
				y++
			case 'D':
				y--
			case 'L':
				x++
			case 'R':
				x--
		}
	}

	return x == 0 && y == 0
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	moves := strings.Replace(temp, "]", "", -1)

	fmt.Printf("moves = %s\n", moves)

	timeStart := time.Now()

	result := judgeCircle(moves)
	fmt.Printf("result = %s\n", strconv.FormatBool(result))

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
