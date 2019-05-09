package main

import (
	"fmt"
	"strings"
	"time"
)

func letterCasePermutation(s string) []string {
	// 104ms
	ans := make([]string, 0)
	formatString(s, 0, "", &ans)
	return ans
}

func formatString(s string, i int, prevString string, ans *[]string) {
	if i >= len(s) {
		*ans = append(*ans, prevString)
		return
	}
	if s[i] >= 48 && s[i] <= 57 {
		formatString(s, i+1, prevString+string(s[i]), ans)
	} else if s[i] >= 65 && s[i] <= 90 {

		formatString(s, i+1, prevString+string(s[i]+byte(32)), ans)
		formatString(s, i+1, prevString+string(s[i]), ans)
	} else {
		formatString(s, i+1, prevString+string(s[i]-byte(32)), ans)
		formatString(s, i+1, prevString+string(s[i]), ans)
	}
}

func letterCasePermutation2(S string) []string {
	// 104ms
	seen := make(map[string]bool)
	var dfs func(s string, curIdx int)
	dfs = func(s string, curIdx int) {
		if _, x := seen[s]; x {
			return
		}
		seen[s] = true
		// try all possibilties
		for i := curIdx; i < len(s); i++ {
			if s[i] >= 97 && s[i] <= 122 {
				// clone
				clone := ""
				clone += s[:i]
				clone += string(s[i] - 32)
				clone += s[i+1:]
				dfs(clone, curIdx+1)
			} else if s[i] >= 65 && s[i] <= 90 {
				// clone
				clone := ""
				clone += s[:i]
				clone += string(s[i] + 32)
				clone += s[i+1:]
				dfs(clone, curIdx+1)
			} else {
				dfs(s, curIdx+1)
			}
		}
	}
	dfs(S, 0)
	res := []string{}
	for key := range seen {
		res = append(res, key)
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	S := strings.Replace(temp, "]", "", -1)

	fmt.Printf("S = %s\n", S)

	timeStart := time.Now()

	result := letterCasePermutation(S)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
