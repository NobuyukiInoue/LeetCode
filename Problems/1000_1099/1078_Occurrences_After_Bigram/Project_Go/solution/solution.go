package solution

import (
	"fmt"
	"strings"
	"time"
)

func findOcurrences(text string, first string, second string) []string {
	// 0ms
	words := strings.Split(text, " ")
	ans := make([]string, 0)
	for i := 2; i < len(words); i++ {
		if words[i-2] == first && words[i-1] == second {
			ans = append(ans, words[i])
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")
	text, first, second := flds[0], flds[1], flds[2]

	fmt.Printf("text = %s, first = %s, second = %s\n", text, first, second)

	timeStart := time.Now()

	result := findOcurrences(text, first, second)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
