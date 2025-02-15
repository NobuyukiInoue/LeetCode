package solution

import (
	"fmt"
	"strings"
	"time"
)

func possibleStringCount(word string) int {
	// 0ms
	ans, prev := 0, word[0]
	for i := 0; i < len(word); i++ {
		if word[i] == prev {
			ans++
		}
		prev = word[i]
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	word := strings.Replace(temp, "]", "", -1)
	fmt.Printf("word = \"%s\"\n", word)

	timeStart := time.Now()

	result := possibleStringCount(word)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
