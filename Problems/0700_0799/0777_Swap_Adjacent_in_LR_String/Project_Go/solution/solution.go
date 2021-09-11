package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func canTransform(start string, end string) bool {
	// 4ms
	if strings.Replace(start, "X", "", -1) != strings.Replace(end, "X", "", -1) {
		return false
	}
	pointer1, pointer2 := 0, 0
	m, n := len(start), len(end)
	for pointer1 < m && pointer2 < n {
		for pointer1 < m && start[pointer1] == 'X' {
			pointer1 += 1
		}
		for pointer2 < n && end[pointer2] == 'X' {
			pointer2 += 1
		}
		if pointer1 == m && pointer2 == n {
			return true
		}
		if pointer1 == m || pointer2 == n {
			return false
		}
		if start[pointer1] != end[pointer2] {
			return false
		}
		if start[pointer1] == 'L' && pointer2 > pointer1 {
			return false
		}
		if end[pointer2] == 'R' && pointer1 > pointer2 {
			return false
		}
		pointer1++
		pointer2++
	}
	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	start, end := flds[0], flds[1]
	fmt.Printf("s = \"%s\", end = \"%s\"\n", start, end)

	timeStart := time.Now()

	result := canTransform(start, end)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
