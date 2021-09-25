package solution

import (
	"fmt"
	"sort"
	"strings"
	"time"
)

func longestStrChain(words []string) int {
	// 16ms
	sort.Slice(words, func(i, j int) bool {
		return len(words[i]) < len(words[j])
	})
	m, res := make(map[string]int, len(words)), 0
	for _, word := range words {
		l := 1
		for i := 0; i < len(word); i++ {
			if k := m[word[:i]+word[i+1:]] + 1; k > l {
				l = k
			}
		}
		if l > res {
			res = l
		}
		m[word] = l
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	words := strings.Split(temp, ",")
	fmt.Printf("words = %s\n", words)

	timeStart := time.Now()

	result := longestStrChain(words)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
