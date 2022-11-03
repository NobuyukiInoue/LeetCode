package solution

import (
	"fmt"
	"strings"
	"time"
)

func oddString(words []string) string {
	// 1ms - 3ms
	n := len(words[0])
	for i := 1; i < n; i++ {
		m := map[int][]int{}
		for k, word := range words {
			diff := int(word[i] - word[i-1])
			m[diff] = append(m[diff], k)
		}

		if len(m) == 2 {
			for _, v := range m {
				if len(v) == 1 {
					return words[v[0]]
				}
			}
		}
	}
	return words[0]
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	words := strings.Split(temp, ",")

	fmt.Printf("words = %s\n", StringArrayToString(words))

	timeStart := time.Now()

	result := oddString(words)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
