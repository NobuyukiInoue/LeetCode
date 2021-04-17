package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func truncateSentence(s string, k int) string {
	// 0ms
	n, sLength := 0, len(s)
	for i := 0; i < len(s); i++ {
		if s[i] == ' ' {
			n++
		}
		if n == k {
			sLength = i
			break
		}
	}
	return s[:sLength]
}

func truncateSentence2(s string, k int) string {
	// 0ms
	flds := strings.Split(s, " ")
	if k < 1 {
		return ""
	}
	res := flds[0]
	for i := 1; i < k; i++ {
		res += " " + flds[i]
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
	fmt.Printf("s = \"%s\", k = %d\n", s, k)

	timeStart := time.Now()

	result := truncateSentence(s, k)

	timeEnd := time.Now()

	fmt.Printf("result = \"%s\"\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
