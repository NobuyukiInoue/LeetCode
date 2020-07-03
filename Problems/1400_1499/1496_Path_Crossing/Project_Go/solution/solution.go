package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func isPathCrossing(path string) bool {
	// 0ms
	pos := make(map[string] bool)
	x, y := 0, 0
	pos["0,0"] = true
	for _, v := range path {
		if v == 'N' {
			x++
		}
		if v == 'E' {
			y++
		}
		if v == 'W' {
			y--
		}
		if v == 'S' {
			x--
		}

		key := fmt.Sprintf("%d,%d", x, y)

		_, exist := pos[key]
		if exist {
			return true
		}

		pos[key] = true
	}

	return false
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	path := strings.Replace(temp, "]", "", -1)
	fmt.Printf("path = %s\n", path)

	timeStart := time.Now()

	result := isPathCrossing(path)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
