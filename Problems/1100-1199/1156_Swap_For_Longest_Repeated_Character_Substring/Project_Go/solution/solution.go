package solution

import (
	"fmt"
	"strings"
	"time"
)

func maxRepOpt1(text string) int {
	// 0ms
	dic := make([]int, 26)
	max := 0
	for _, c := range text {
		dic[c-'a']++
		max = myMax(max, dic[c-'a'])
	}

	if max <= 1 {
		return max
	}
	max = 1
	n := len(text)
	var j, k int
	for i := 0; i < n; i = j {
		cur := text[i]
		for j = i; j < n && text[j] == cur; j++ {
		}
		for k = j + 1; k < n && text[k] == cur; k++ {
		}
		if k-i-1 == dic[cur-'a'] {
			max = myMax(max, k-i-1)
		} else {
			max = myMax(max, k-i)
		}
	}

	return max
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	text := strings.Replace(temp, "]", "", -1)

	fmt.Printf("text = %s\n", text)
	timeStart := time.Now()

	result := maxRepOpt1(text)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
