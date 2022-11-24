package solution

import (
	"fmt"
	"strings"
	"time"
)

func wordBreak(s string, wordDict []string) []string {
	// 1ms
	dict := make(map[string]bool)
	for _, w := range wordDict {
		dict[w] = true
	}

	mem := make(map[int][]string)
	return dfs(s, dict, mem)
}

func dfs(s string, dict map[string]bool, mem map[int][]string) []string {
	if v, exist := mem[len(s)]; exist {
		return v
	}
	retSlice := make([]string, 0)
	for i := 1; i <= len(s); i++ {
		if dict[s[:i]] {
			sliceV := dfs(s[i:], dict, mem)
			for _, v := range sliceV {
				retSlice = append(retSlice, s[:i]+" "+v)
			}
			if i == len(s) {
				retSlice = append(retSlice, s)
			}
		}
	}
	mem[len(s)] = retSlice
	return retSlice
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	s := flds[0]
	wordDict := strings.Split(flds[1], ",")
	fmt.Printf("s = \"%s\", wordDict = \"%s\"\n", s, wordDict)

	timeStart := time.Now()

	result := wordBreak(s, wordDict)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", StringArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
