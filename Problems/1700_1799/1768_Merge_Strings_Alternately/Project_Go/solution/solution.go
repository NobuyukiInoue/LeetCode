package solution

import (
	"fmt"
	"strings"
	"time"
)

func mergeAlternately(word1 string, word2 string) string {
	// 0ms
	minLen := myMin(len(word1), len(word2))
	res := ""
	for i := 0; i < minLen; i++ {
		res += string(word1[i]) + string(word2[i])
	}
	res += word1[minLen:] + word2[minLen:]
	return res
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
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	word1, word2 := flds[0], flds[1]
	fmt.Printf("word1 = %s, word2 = %s\n", word1, word2)

	timeStart := time.Now()

	result := mergeAlternately(word1, word2)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
