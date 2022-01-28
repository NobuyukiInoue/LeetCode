package solution

import (
	"bytes"
	"fmt"
	"math"
	"strconv"
	"strings"
	"time"
)

func divideString(s string, k int, fill byte) []string {
	// 0ms
	res := make([]string, int(math.Ceil(float64(len(s))/float64(k))))
	pos := 0
	var i int
	for i = 0; pos+k <= len(s); i++ {
		res[i] = s[pos : pos+k]
		pos += k
	}
	if pos < len(s) {
		res[i] = s[pos:]
		fills := make([]byte, 1)
		fills[0] = fill
		res[i] += string(bytes.Repeat(fills, k-len(res[i])))
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	s := flds[0]
	k, _ := strconv.Atoi(flds[1])
	fill := flds[2][0]
	fmt.Printf("s = \"%s\", k = %d, fill = \"%c\"\n", s, k, fill)

	timeStart := time.Now()

	result := divideString(s, k, fill)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
