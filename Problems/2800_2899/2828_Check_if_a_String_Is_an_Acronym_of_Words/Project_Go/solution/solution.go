package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
	//	"golang.org/x/exp/slices"
)

func isAcronym(words []string, s string) bool {
	// 4ms - 11ms
	if len(words) != len(s) {
		return false
	}
	for i, word := range words {
		if word[0] != s[i] {
			return false
		}
	}
	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, ", ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	words := strings.Split(flds[0], ",")
	s := flds[1]
	fmt.Printf("words = %s, s = %s\n", StringArrayToString(words), s)

	timeStart := time.Now()

	result := isAcronym(words, s)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
