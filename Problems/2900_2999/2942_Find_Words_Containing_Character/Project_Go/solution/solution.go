package solution

import (
	"fmt"
	"strings"
	"time"
)

func findWordsContaining(words []string, x byte) []int {
	// 5ms - 7ms
	var ans []int
	xStr := string(x)
	for i, word := range words {
		if strings.Contains(word, xStr) {
			ans = append(ans, i)
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	words := strings.Split(flds[0], ",")
	x := flds[1][0]
	fmt.Printf("words = %s, x = %c\n", words, x)

	timeStart := time.Now()

	result := findWordsContaining(words, x)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
