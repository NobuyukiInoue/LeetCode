package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func isRobotBounded(instructions string) bool {
	x, y, i := 0, 0, 0
	d := [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
	for j := 0; j < len(instructions); j++ {
		if instructions[j] == 'R' {
			i = (i + 1) % 4
		} else if instructions[j] == 'L' {
			i = (i + 3) % 4
		} else {
			x += d[i][0]
			y += d[i][1]
		}
	}

	return x == 0 && y == 0 || i > 0
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[", "", -1)
	instructions := strings.Replace(temp, "]", "", -1)

	fmt.Printf("instructions = %s\n", instructions)

	timeStart := time.Now()

	result := isRobotBounded(instructions)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
