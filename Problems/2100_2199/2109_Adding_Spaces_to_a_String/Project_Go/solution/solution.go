package solution

import (
	"fmt"
	"strings"
	"time"
)

func addSpaces(s string, spaces []int) string {
	// 118ms - 119ms
	var stringBuffer strings.Builder
	space_idx := 0
	for src := 0; src < len(s); src++ {
		if space_idx < len(spaces) && src == spaces[space_idx] {
			stringBuffer.WriteString(" ")
			space_idx++
		}
		stringBuffer.Write([]byte{s[src]})
	}
	return stringBuffer.String()
}

func addSpaces_bad(s string, spaces []int) string {
	// Time Limit Exceeded.
	res, pre := "", 0
	for _, pos := range spaces {
		res += s[pre:pos] + " "
		pre = pos
	}
	res += s[pre:]
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, ", ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	s := flds[0]
	spaces := StringToIntArray(flds[1])
	fmt.Printf("s = \"%s\", spaces = [%s]\n", s, IntArrayToString(spaces))

	timeStart := time.Now()

	result := addSpaces(s, spaces)

	timeEnd := time.Now()

	fmt.Printf("result = \"%s\"\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
