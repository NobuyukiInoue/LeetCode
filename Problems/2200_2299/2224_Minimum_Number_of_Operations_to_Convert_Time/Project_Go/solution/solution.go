package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func convertTime(current string, correct string) int {
	// 0ms
	currentHour, _ := strconv.Atoi(current[:2])
	correctHour, _ := strconv.Atoi(correct[:2])
	currentMinutes, _ := strconv.Atoi(current[3:])
	correctMinutes, _ := strconv.Atoi(correct[3:])
	result, minutes := 0, (correctHour-currentHour)*60-(currentMinutes-correctMinutes)
	for _, increase := range []int{60, 15, 5} {
		result += minutes / increase
		minutes %= increase
	}
	return result + minutes
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")
	current, correct := flds[0], flds[1]
	fmt.Printf("current = %s, correct = %s\n", current, correct)

	timeStart := time.Now()

	result := convertTime(current, correct)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
