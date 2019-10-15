package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func isAlienSorted(words []string, order string) bool {
	base, index := words[0], 0
	for i := 1; i < len(words); i++ {
		min := min(len(base), len(words[i]))
		for index < min && base[index] == words[i][index] {
			index++
		}
		if index == len(words[i]) {
			return false
		}
		if strings.Index(order, string(base[index])) > strings.Index(order, string(words[i][index])) {
			return false
		} else {
			base = words[i]
		}
	}
	return true
}

func min(a int, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	words := strings.Split(flds[0], ",")
	order := flds[1]
	fmt.Printf("words = %s, order = %s\n", words, order)

	timeStart := time.Now()

	result := isAlienSorted(words, order)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
