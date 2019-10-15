package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func isSubsequence(s string, t string) bool {
	var si, ti int
	if len(s) == 0 {
		return true
	}
	for {
		if ti == len(t) {
			return false
		}
		if s[si] == t[ti] {
			si++
			ti++
			if si == len(s) {
				return true
			}
			continue
		}
		ti++
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")
	s, t := flds[0], flds[1]

	fmt.Printf("s = %s, t = %s\n", s, t)

	timeStart := time.Now()

	result := isSubsequence(s, t)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
