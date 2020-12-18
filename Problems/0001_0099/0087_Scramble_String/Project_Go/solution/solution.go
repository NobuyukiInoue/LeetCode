package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

type sortRunes []rune

func (s sortRunes) Less(i, j int) bool {
	return s[i] < s[j]
}

func (s sortRunes) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}

func (s sortRunes) Len() int {
	return len(s)
}

func SortString(s string) string {
	r := []rune(s)
	sort.Sort(sortRunes(r))
	return string(r)
}

func isScramble(s1 string, s2 string) bool {
	// 4ms
	m, n := len(s1), len(s2)
	sorted_s1, sorted_s2 := SortString(s1), SortString(s2)
	if m != n || sorted_s1 != sorted_s2 {
		return false
	}
	if m < 4 || s1 == s2 {
		return true
	}
	for i := 1; i < n; i++ {
		if isScramble(s1[:i], s2[:i]) && isScramble(s1[i:], s2[i:]) ||
			isScramble(s1[:i], s2[m-i:]) && isScramble(s1[i:], s2[:n-i]) {
			return true
		}
	}
	return false
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	s1 := flds[0]
	s2 := flds[1]
	fmt.Printf("s1 = %s, s2 = %s\n", s1, s2)

	timeStart := time.Now()

	result := isScramble(s1, s2)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
