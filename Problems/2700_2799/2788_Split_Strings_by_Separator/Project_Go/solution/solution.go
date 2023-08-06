package solution

import (
	"fmt"
	"strings"
	"time"
	//	"golang.org/x/exp/slices"
)

func splitWordsBySeparator(words []string, separator byte) []string {
	// 12ms - 22m
	var ans []string
	for _, word := range words {
		flds := strings.Split(word, string(separator))
		for _, fld := range flds {
			if fld != "" {
				ans = append(ans, fld)
			}
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, ", ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	words := strings.Split(flds[0], ",")
	separator := flds[1][0]
	fmt.Printf("words = %s, separator = %c\n", StringArrayToString(words), separator)

	timeStart := time.Now()

	result := splitWordsBySeparator(words, separator)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
