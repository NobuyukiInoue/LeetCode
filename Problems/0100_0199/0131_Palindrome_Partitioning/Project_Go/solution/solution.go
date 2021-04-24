package solution

import (
	"fmt"
	"strings"
	"time"
)

func partition(s string) [][]string {
	// 336ms
	var ret [][]string
	helper(s, 0, []string{}, &ret)
	return ret
}

func helper(s string, start int, temp []string, ret *[][]string) {
	if start == len(s) {
		*ret = append(*ret, append([]string{}, temp...))
		return
	}
	for i := start; i < len(s); i++ {
		if !isPalindrome(s[start : i+1]) {
			continue
		}
		temp = append(temp, s[start:i+1])
		helper(s, i+1, temp, ret)
		temp = temp[:len(temp)-1]
	}
}

func isPalindrome(s string) bool {
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		if s[i] != s[j] {
			return false
		}
	}
	return true
}

func partition2(s string) [][]string {
	// 336ms
	res := make([][]string, 0)
	dp := make([][]bool, len(s))
	for i := 0; i < len(dp); i++ {
		dp[i] = make([]bool, len(s))
	}

	for i := 0; i < len(s); i++ {
		for j := 0; j <= i; j++ {
			if s[i] == s[j] && (i-j <= 2 || dp[j+1][i-1]) {
				dp[j][i] = true
			}
		}
	}
	helper2(s, &res, &dp, &[]string{}, 0)
	return res
}

func helper2(s string, res *[][]string, dp *[][]bool, path *[]string, pos int) {
	if pos == len(s) {
		temp := make([]string, len(*path))
		copy(temp, *path)
		*res = append(*res, temp)
		return
	}

	for i := pos; i < len(s); i++ {
		if (*dp)[pos][i] {
			*path = append(*path, s[pos:i+1])
			helper2(s, res, dp, path, i+1)
			*path = (*path)[:len(*path)-1]
		}
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := partition(s)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
