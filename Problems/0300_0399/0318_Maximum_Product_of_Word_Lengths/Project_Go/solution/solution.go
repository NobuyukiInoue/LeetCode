package solution

import (
	"fmt"
	"strings"
	"time"
)

func maxProduct(words []string) int {
	// 12ms
	var max int
	masks := make([]int64, len(words))
	for i := range words {
		for j := range words[i] {
			masks[i] |= 1 << (words[i][j] - 'a')
		}
	}
	for i := range masks {
		for j := range masks {
			if masks[i]&masks[j] == 0 && max < len(words[i])*len(words[j]) {
				max = len(words[i]) * len(words[j])
			}
		}
	}
	return max
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	words := strings.Split(temp, ",")

	fmt.Printf("words = %s\n", words)
	timeStart := time.Now()

	result := maxProduct(words)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
