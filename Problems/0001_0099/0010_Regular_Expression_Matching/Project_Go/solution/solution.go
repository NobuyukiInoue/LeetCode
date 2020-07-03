package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func isMatch(s string, p string) bool {
	// 0ms
	memo := make([][]int, len(s)+1)
	for i := 0; i < len(memo); i++ {
		memo[i] = make([]int, len(p))
	}

	return isMatch2(s, 0, p, 0, memo)
}

func isMatch2(s string, matchedLengthS int, p string, matchedLengthP int, memo [][]int) bool {
	if matchedLengthS == len(s) && matchedLengthP == len(p) {
		return true
	}

	if matchedLengthP == len(p) {
		return false
	}

	if memo[matchedLengthS][matchedLengthP] != 0 {
		return memo[matchedLengthS][matchedLengthP] == 1
	}

	if matchedLengthP+1 < len(p) && p[matchedLengthP+1] == '*' {
		if matchedLengthS < len(s) && (p[matchedLengthP] == s[matchedLengthS] || p[matchedLengthP] == '.') {
			if isMatch2(s, matchedLengthS+1, p, matchedLengthP, memo) || isMatch2(s, matchedLengthS+1, p, matchedLengthP+2, memo) || isMatch2(s, matchedLengthS, p, matchedLengthP+2, memo) {
				memo[matchedLengthS][matchedLengthP] = 1
			}
		} else {
			if isMatch2(s, matchedLengthS, p, matchedLengthP+2, memo) {
				memo[matchedLengthS][matchedLengthP] = 1
			}
		}
	} else {
		if matchedLengthS < len(s) && (p[matchedLengthP] == s[matchedLengthS] || p[matchedLengthP] == '.') {
			if isMatch2(s, matchedLengthS+1, p, matchedLengthP+1, memo) {
				memo[matchedLengthS][matchedLengthP] = 1
			}
		}
	}

	if memo[matchedLengthS][matchedLengthP] == 0 {
		memo[matchedLengthS][matchedLengthP] = -1
	}

	return memo[matchedLengthS][matchedLengthP] == 1
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

	s, p := flds[0], flds[1]
	fmt.Printf("s = \"%s\", p = \"%s\"\n", s, p)

	timeStart := time.Now()

	result := isMatch(s, p)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
