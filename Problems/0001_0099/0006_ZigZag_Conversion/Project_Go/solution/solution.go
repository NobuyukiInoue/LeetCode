package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func convert(s string, numRows int) string {
	// 0ms
	if numRows <= 1 {
		return s
	}

	runes := []rune(s)
	n := len(runes)
	runesOut := make([]rune, n)
	j := 0
	for row := 0; row < numRows; row++ {
		k := row
		skip := 2 * (numRows - row - 1)
		for j < n && k < n {
			if skip > 0 {
				runesOut[j] = runes[k]
				k = k + skip
				j++
			}
			skip = 2*(numRows-1) - skip
		}
	}
	return string(runesOut)
}

func checkPalindrome(s string, i int, j int, max string) string {
	leng := len(s)
	var sub string
	for i >= 0 && j <= (leng-1) && s[i] == s[j] {
		sub = s[i : j+1]
		i--
		j++
	}
	if len(max) < len(sub) {
		max = sub
	}
	return max
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	s := flds[0]
	numRows, _ := strconv.Atoi(flds[1]);
	fmt.Printf("s = %s, numRows = %d\n", s, numRows)

	timeStart := time.Now()

	result := convert(s, numRows)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
