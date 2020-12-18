package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func camelMatch(queries []string, pattern string) []bool {
	// 0ms
	res := make([]bool, len(queries))
	for i, query := range(queries) {
		res[i] = isMatch(query, pattern)
	}
	return res
}

func isMatch(query string, pattern string) bool {
	i := 0
	for _, ch := range(query) {
		if i < len(pattern) && ch == rune(pattern[i]) {
			i++
		} else if ch < 'a' {
			return false
		}
	}
	return i == len(pattern)
}

func BoolArrayToString(nums []bool) string {
	if len(nums) <= 0 {
		return ""
	}

	resultStr := strconv.FormatBool(nums[0])
	for i := 1; i < len(nums); i++ {
		resultStr += ", " + strconv.FormatBool(nums[i])
	}

	return resultStr
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	queries := strings.Split(flds[0], ",")
	pattern := flds[1]
	fmt.Printf("queries = %s\n", StringArrayToString(queries))
	fmt.Printf("pattern = %s\n", pattern)

	timeStart := time.Now()

	result := camelMatch(queries, pattern)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", BoolArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
