package solution

import (
	"fmt"
	"strings"
	"time"
)

func maxNumberOfBalloons(text string) int {
	// 0ms
	count := make([]int, 26)
	countBallon := make([]int, 26)
	result := len(text)
	for i := 0; i < result; i++ {
		count[text[i]-'a']++
	}
	targetStr := "balloon"
	for _, c := range targetStr {
		countBallon[c-'a']++
	}
	for _, c := range targetStr {
		result = min(result, count[c-'a']/countBallon[c-'a'])
	}

	return result
}

func min(a int, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	text := strings.Replace(temp, "]", "", -1)

	fmt.Printf("text = %s\n", text)
	timeStart := time.Now()

	result := maxNumberOfBalloons(text)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
