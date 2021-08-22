package solution

import (
	"fmt"
	"strings"
	"time"
)

func minTimeToType(word string) int {
	// 0ms
	cnt, prev := len(word), 'a'
	for _, cur := range word {
		diff := myAbs(int(cur - prev))
		cnt += myMin(diff, 26-diff)
		prev = cur
	}
	return cnt
}

func myAbs(num int) int {
	if num >= 0 {
		return num
	}
	return -num
}

func myMin(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	word := strings.Replace(temp, "]", "", -1)
	fmt.Printf("word = %s\n", word)

	timeStart := time.Now()

	result := minTimeToType(word)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
