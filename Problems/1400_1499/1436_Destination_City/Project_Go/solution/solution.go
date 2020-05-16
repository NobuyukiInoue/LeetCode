package solution

import (
	"fmt"
	"strings"
	"time"
)

func destCity(paths [][]string) string {
	// 4ms
	dic := make(map[string]string, len(paths))
	var res string

	for i := 0; i < len(paths); i++ {
		dic[paths[i][0]] = paths[i][0]
	}

	for i := 0; i < len(paths); i++ {
		_, exists := dic[paths[i][1]]
		if !exists {
			res = paths[i][1]
			break
		}
	}

	return res
}

func strArrayToString(data []string) string {
	if len(data) <= 0 {
		return ""
	}

	res := "[" + data[0]
	for i := 1; i < len(data); i++ {
		res += ", \"" + data[i] + "\""
	}

	return res + "]"
}

func strArrayArrayToString(data [][]string) string {
	if len(data) <= 0 {
		return ""
	}

	res := strArrayToString(data[0])
	for i := 1; i < len(data); i++ {
		res += ", " + strArrayToString(data[i])
	}

	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	flds := strings.Replace(temp, "]]", "", -1)
	data := strings.Split(flds, "],[")

	paths := make([][]string, len(data))
	for i := 0; i < len(data); i++ {
		paths[i] = strings.Split(data[i], ",")
	}

	fmt.Printf("paths = [%s]\n", strArrayArrayToString(paths))
	timeStart := time.Now()

	result := destCity(paths)

	timeEnd := time.Now()

	fmt.Printf("result = \"%s\"\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
