package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func longestSubstring(s string, k int) int {
	// 0ms
	return longest(s, 0, len(s)-1, k)
}

func longest(s string, start int, end int, k int) int {
	if start > end {
		return 0
	}

	len := end - start + 1
	if len == 0 || k > len {
		return 0
	}
	if k <= 1 {
		return len
	}

	alcount := make([]int, 'z'-'a'+1)

	var i int
	for i = start; i <= end; i++ {
		alcount[s[i]-'a']++
	}

	i = start
	for i <= end && alcount[s[i]-'a'] >= k {
		i++
	}

	if i >= end {
		return i - start
	}

	ls1 := longest(s, start, i-1, k)
	for i <= end && alcount[s[i]-'a'] < k {
		i++
	}

	var ls2 int
	if i <= end {
		ls2 = longest(s, i, end, k)
	} else {
		ls2 = 0
	}
	return myMax(ls1, ls2)
}

func myMax(a int, b int) int {
	if a > b {
		return a
	}
	return b
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

	result := longestSubstring(s, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
