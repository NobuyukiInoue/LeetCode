package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func finalPositionOfSnake(n int, commands []string) int {
	// 3ms
	x, y := 0, 0
	for _, cmd := range commands {
		switch cmd {
		case "LEFT":
			y--
		case "RIGHT":
			y++
		case "UP":
			x--
		default:
			x++
		}
	}
	return x*n + y
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	n, _ := strconv.Atoi(flds[0])
	commands := strings.Split(flds[1], ",")
	fmt.Printf("n = %d, commands = %s\n", n, commands)

	timeStart := time.Now()

	result := finalPositionOfSnake(n, commands)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
