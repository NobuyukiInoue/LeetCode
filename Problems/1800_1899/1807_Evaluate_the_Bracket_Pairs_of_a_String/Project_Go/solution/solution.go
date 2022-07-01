package solution

import (
	"fmt"
	"strings"
	"time"
)

func evaluate(s string, knowledge [][]string) string {
	// 210ms - 302ms
	mymap := make(map[string]string, len(knowledge))
	for _, entry := range knowledge {
		mymap[entry[0]] = entry[1]
	}
	var result strings.Builder
	result.Grow(len(s))
	for i := 0; i < len(s); i++ {
		if s[i] == '(' {
			var keyBuilder strings.Builder
			for {
				i++
				if i == len(s) || s[i] == ')' {
					break
				}
				keyBuilder.WriteByte(s[i])
			}
			key := keyBuilder.String()
			if replacement, ok := mymap[key]; ok {
				result.WriteString(replacement)
			} else {
				result.WriteByte('?')
			}
		} else {
			result.WriteByte(s[i])
		}
	}
	return result.String()
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	flds := strings.Split(temp, "],[[")
	s := strings.Replace(flds[0], "[[", "", -1)
	flds1 := strings.Split(strings.Replace(flds[1], "]]]", "", -1), "],[")
	knowledge := make([][]string, len(flds1))
	for i := 0; i < len(knowledge); i++ {
		knowledge[i] = strings.Split(flds1[i], ",")
	}
	fmt.Printf("s = \"%s\", knowledge = %s\n", s, StringStringArrayToString(knowledge))

	timeStart := time.Now()

	result := evaluate(s, knowledge)

	timeEnd := time.Now()

	fmt.Printf("result = \"%s\"\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
