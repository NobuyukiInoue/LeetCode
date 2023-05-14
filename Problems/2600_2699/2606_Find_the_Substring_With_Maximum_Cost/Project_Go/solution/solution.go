package solution

import (
	"fmt"
	"strings"
	"time"
)

func maximumCostSubstring(s string, chars string, vals []int) int {
	// 9ms - 11ms
	var char_dict [26]int
	for i := 0; i < 26; i++ {
		char_dict[i] = i + 1
	}
	for i := 0; i < len(chars); i++ {
		char_dict[chars[i]-'a'] = vals[i]
	}
	max_cost, curr_cost := 0, 0
	for _, ch := range s {
		curr_cost += char_dict[ch-'a']
		if curr_cost < 0 {
			curr_cost = 0
		}
		if curr_cost > max_cost {
			max_cost = curr_cost
		}
	}
	return max_cost
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, ", ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	s, chars := flds[0], flds[1]
	vals := StringToIntArray(flds[2])
	fmt.Printf("s = \"%s\", chars = \"%s\", vals = [%s]\n", s, chars, IntArrayToString(vals))

	timeStart := time.Now()

	result := maximumCostSubstring(s, chars, vals)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
