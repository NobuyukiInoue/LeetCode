package solution

import (
	"fmt"
	"strings"
	"time"
)

func cellsInRange(s string) []string {
	// 8ms
	col1, col2 := s[0], s[3]
	row1, row2 := s[1], s[4]
	var ans []string
	for col := col1; col <= col2; col++ {
		for row := row1; row <= row2; row++ {
			ans = append(ans, fmt.Sprintf("%c%c", col, row))
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := cellsInRange(s)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
