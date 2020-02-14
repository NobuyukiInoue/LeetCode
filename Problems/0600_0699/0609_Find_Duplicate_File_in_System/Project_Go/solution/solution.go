package solution

import (
	"fmt"
	"strings"
	"time"
)

func findDuplicate(paths []string) [][]string {
	// 32ms
	cache := make(map[string][]string)
	for _, path := range paths {
		parts := strings.Split(path, " ")
		dir := parts[0]
		for i := 1; i < len(parts); i++ {
			bracketPosition := strings.IndexByte(parts[i], '(')
			content := parts[i][bracketPosition+1 : len(parts[i])-1]
			cache[content] = append(cache[content], dir+"/"+parts[i][:bracketPosition])
		}
	}
	result := make([][]string, 0, len(cache))
	for _, group := range cache {
		if len(group) < 2 {
			continue
		}
		result = append(result, group)
	}
	return result
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)

	paths := strings.Split(temp, ",")
	fmt.Printf("paths = [%s]\n", paths)

	timeStart := time.Now()

	result := findDuplicate(paths)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
