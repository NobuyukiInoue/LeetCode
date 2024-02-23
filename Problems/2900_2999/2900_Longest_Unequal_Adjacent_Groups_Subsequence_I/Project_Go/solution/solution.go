package solution

import (
	"fmt"
	"strings"
	"time"
)

func getLongestSubsequence(words []string, groups []int) []string {
	// 3ms - 4ms
	ans := []string{words[0]}
	for i := 1; i < len(words); i++ {
		if groups[i] == groups[i-1] {
			continue
		}
		ans = append(ans, words[i])
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
	groups := StringToIntArray(flds[1])
	fmt.Printf("words = [%s], groups = [%s]\n", StringArrayToString(words), IntArrayToString(groups))

	timeStart := time.Now()

	result := getLongestSubsequence(words, groups)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", StringArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
