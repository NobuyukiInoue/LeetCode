package solution

import (
	"fmt"
	"strings"
	"time"
)

func minOperations(boxes string) []int {
	// 4ms - 6ms
	total, move_count := 0, 0
	res := make([]int, len(boxes))
	for i, _ := range boxes {
		res[i] = move_count
		if boxes[i] == '1' {
			total++
		}
		move_count += total
	}
	total, move_count = 0, 0
	for i := len(boxes) - 1; i >= 0; i-- {
		res[i] += move_count
		if boxes[i] == '1' {
			total++
		}
		move_count += total
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	boxes := strings.Replace(temp, "]", "", -1)
	fmt.Printf("boxes = \"%s\"\n", boxes)

	timeStart := time.Now()

	result := minOperations(boxes)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
