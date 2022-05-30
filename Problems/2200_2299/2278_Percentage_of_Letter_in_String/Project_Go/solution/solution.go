package solution

import (
	"fmt"
	"strings"
	"time"
)

func percentageLetter(s string, letter byte) int {
	// 0ms
	cnt := 0
	for _, ch := range s {
		if byte(ch) == letter {
			cnt++
		}
	}
	return 100 * cnt / len(s)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")
	s, letter := flds[0], flds[1][0]
	fmt.Printf("s = %s, letter = %c\n", s, letter)

	timeStart := time.Now()

	result := percentageLetter(s, letter)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
