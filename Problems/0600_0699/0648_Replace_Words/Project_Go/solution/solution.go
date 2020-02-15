package solution

import (
	"fmt"
	"strings"
	"time"
)

func replaceWords(dict []string, sentence string) string {
	// 12ms
	magic := make(map[string]interface{})
	max, min := 0, 1000
	for _, v := range dict {
		magic[v] = nil
		l := len(v)
		if l > max {
			max = l
		}
		if l < min {
			min = l
		}
	}
	fields := strings.Fields(sentence)
	for i, v := range fields {
		// j < len(v) is better than j ≤ len(v)
		for j := min; j < len(v) && j <= max; j++ {
			vs := v[:j]
			if _, exist := magic[vs]; exist {
				fmt.Println(fields[i], vs)
				fields[i] = vs
				break
			}
		}
	}
	return strings.Join(fields, " ")
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)

	flds := strings.Split(temp, "],[")
	dict := strings.Split(flds[0], ",")
	sentence := flds[1]
	fmt.Printf("dict = [%s]\n", dict)
	fmt.Printf("sentence = [%s]\n", sentence)

	timeStart := time.Now()

	result := replaceWords(dict, sentence)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
