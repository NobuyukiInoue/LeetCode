package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func getEncryptedString(s string, k int) string {
	// 0ms - 4ms
	k %= len(s)
	return s[k:] + s[:k]
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	s := strings.Replace(flds[0], "\"", "", -1)
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("n = \"%s\", k = %d\n", s, k)

	timeStart := time.Now()

	result := getEncryptedString(s, k)

	timeEnd := time.Now()

	fmt.Printf("result = \"%s\"\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
