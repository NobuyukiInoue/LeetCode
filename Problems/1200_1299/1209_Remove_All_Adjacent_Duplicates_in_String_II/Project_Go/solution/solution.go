package solution

import (
	"bytes"
	"fmt"
	"strconv"
	"strings"
	"time"
)

func removeDuplicates(s string, k int) string {
	// 25ms - 36ms
	if len(s) < k {
		return s
	}
	var st [][]int
	for _, ch := range s {
		if len(st) > 0 && int(ch) == st[len(st)-1][0] {
			st[len(st)-1][1]++
			if st[len(st)-1][1] == k {
				st = st[:len(st)-1]
			}
		} else {
			st = append(st, []int{int(ch), 1})
		}
	}
	res := ""
	for _, cur := range st {
		res += string(bytes.Repeat([]byte{byte(cur[0])}, cur[1]))
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	s := flds[0]
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("s = \"%s\", k = %d\n", s, k)

	timeStart := time.Now()

	result := removeDuplicates(s, k)

	timeEnd := time.Now()

	fmt.Printf("result = \"%s\"\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
