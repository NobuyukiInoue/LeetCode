package solution

import (
	"fmt"
	"strings"
	"time"
)

func countPrefixes(words []string, s string) int {
	// 5ms - 8ms
	ans := 0
	for _, word := range words {
		if strings.Index(s, word) == 0 {
			ans++
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	words, s := strings.Split(flds[0], ","), flds[1]
	fmt.Printf("words = [%s], s = %s\n", words, s)

	timeStart := time.Now()

	result := countPrefixes(words, s)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
