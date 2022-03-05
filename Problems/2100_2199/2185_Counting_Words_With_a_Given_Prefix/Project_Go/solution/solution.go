package solution

import (
	"fmt"
	"strings"
	"time"
)

func prefixCount(words []string, pref string) int {
	// 0ms
	ans, len_pref := 0, len(pref)
	for _, word := range words {
		if len_pref <= len(word) && word[:len_pref] == pref {
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
	words, pref := strings.Split(flds[0], ","), flds[1]
	fmt.Printf("words = [%s], pref = %s\n", words, pref)

	timeStart := time.Now()

	result := prefixCount(words, pref)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
