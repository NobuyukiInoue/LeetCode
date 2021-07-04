package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func isSumEqual(firstWord string, secondWord string, targetWord string) bool {
	// 0ms
	s := ""
	for _, ch := range firstWord {
		s += string(ch - 'a' + '0')
	}
	first, _ := strconv.Atoi(s)

	s = ""
	for _, ch := range secondWord {
		s += string(ch - 'a' + '0')
	}
	second, _ := strconv.Atoi(s)

	s = ""
	for _, ch := range targetWord {
		s += string(ch - 'a' + '0')
	}
	target, _ := strconv.Atoi(s)

	return first+second == target
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	firstWord, secondWord, targetWord := flds[0], flds[1], flds[2]
	fmt.Printf("firstWord = %s, secondWord = %s, targetWord = %s\n", firstWord, secondWord, targetWord)

	timeStart := time.Now()

	result := isSumEqual(firstWord, secondWord, targetWord)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
