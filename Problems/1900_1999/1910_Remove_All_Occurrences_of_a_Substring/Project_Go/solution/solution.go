package solution

import (
	"fmt"
	"strings"
	"time"
)

func removeOccurrences(s string, part string) string {
	// 0ms
	len_part := len(part)
	pos := strings.Index(s, part)
	for pos >= 0 {
		s = s[:pos] + s[pos+len_part:]
		pos = strings.Index(s, part)
	}
	return s
}

/*
func removeOccurrences2(s string, part string) string {
	// 3ms
	for strings.Contains(s, part) {
		s = strings.Replace(s, part, "", 1)
	}
	return s
}
*/

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, ", ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	s, part := flds[0], flds[1]
	fmt.Printf("s = \"%s\", part = \"%s\"\n", s, part)

	timeStart := time.Now()

	result := removeOccurrences(s, part)

	timeEnd := time.Now()

	fmt.Printf("result = \"%s\"\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
