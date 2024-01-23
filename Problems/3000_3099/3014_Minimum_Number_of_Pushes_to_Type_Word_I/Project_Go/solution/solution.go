package solution

import (
	"fmt"
	"strings"
	"time"
)

func minimumPushes(word string) int {
	// 0ms
	n, ans, row := len(word), 0, 1
	for div := n / 8; div > 0; div-- {
		ans += row * 8
		row++
	}
	return ans + (n%8)*row
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	word := strings.Replace(temp, "]", "", -1)
	fmt.Printf("word = \"%s\"\n", word)

	timeStart := time.Now()

	result := minimumPushes(word)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
