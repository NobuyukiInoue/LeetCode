package solution

import (
	"fmt"
	"reflect"
	"strings"
	"time"
)

func findAndReplacePattern(words []string, pattern string) []string {
	// 0ms
	pat := findpat(pattern)
	var res []string
	for _, word := range words {
		if reflect.DeepEqual(findpat(word), pat) {
			res = append(res, word)
		}
	}
	return res
}

func findpat(word string) []int {
	tbl := map[rune]int{}
	m := 0
	pat := make([]int, len(word))
	i := 0
	for _, ch := range word {
		if _, ok := tbl[ch]; !ok {
			m++
			tbl[ch] = m
		}
		pat[i] = tbl[ch]
		i++
	}
	return pat
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	words := strings.Split(flds[0], ",")
	pattern := flds[1]
	fmt.Printf("words = [%s], pattern = %s\n", StringArrayToString(words), pattern)

	timeStart := time.Now()

	result := findAndReplacePattern(words, pattern)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", StringArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
