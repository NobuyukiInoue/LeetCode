package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func hasMatch(s string, p string) bool {
	// 0ms
	index := strings.Index(p, "*")
	p1, p2 := p[:index], p[index+1:]
	if i := strings.Index(s, p1); i > -1 {
		return strings.Index(s[i+len(p1):], p2) > -1
	}
	return false
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	flds := strings.Split(temp, ",")

	s := flds[0]
	p := flds[1]
	fmt.Printf("s = \"%s\", p = \"%s\"\n", s, p)

	timeStart := time.Now()

	result := hasMatch(s, p)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
