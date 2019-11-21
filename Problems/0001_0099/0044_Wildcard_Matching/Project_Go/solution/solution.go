package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func isMatch(s string, p string) bool {
	// 8ms
	m, n := len(s), len(p)
	count := 0

	for i := 0; i < n; i++ {
		if p[i] == '*' {
			count++
		}
	}

	if count == 0 && m != n {
		return false
	} else if n-count > m {
		return false
	}

	match := make([]bool, m+1)
	match[0] = true
	for i := 0; i < m; i++ {
		match[i+1] = false
	}

	for i := 0; i < n; i++ {
		if p[i] == '*' {
			for j := 0; j < m; j++ {
				match[j+1] = match[j] || match[j+1]
			}
		} else {
			for j := m - 1; j >= 0; j-- {
				match[j+1] = (p[i] == '?' || p[i] == s[j]) && match[j]
			}
			match[0] = false
		}
	}

	return match[m]
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	s := flds[0]
	p := flds[1]

	fmt.Printf("s = %s, p = %s\n", s, p)
	timeStart := time.Now()

	result := isMatch(s, p)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
