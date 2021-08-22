package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func isPrefixString(s string, words []string) bool {
	// 0ms
	count := 0
	for _, word := range words {
		for _, ch := range word {
			if count == len(s) {
				return false
			}
			if s[count] != byte(ch) {
				return false
			}
			count++
		}
		if count == len(s) {
			return true
		}
	}
	return count == len(s)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	s := flds[0]
	words := strings.Split(flds[1], ",")
	fmt.Printf("s = \"%s\", words = \"%s\"\n", s, words)

	timeStart := time.Now()

	result := isPrefixString(s, words)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
