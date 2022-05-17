package solution

import (
	"fmt"
	"strings"
	"time"
)

func removeDigit(number string, digit byte) string {
	// 0ms - 4ms
	position := -1
	for i := 0; i < len(number)-1; i++ {
		if number[i] == digit && number[i] < number[i+1] {
			position = i
			break
		}
	}
	if position == -1 {
		position = strings.LastIndex(number, string(digit))
	}
	return number[0:position] + number[position+1:]
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")
	number, digit := flds[0], flds[1][0]
	fmt.Printf("number = %s, digit = %c\n", number, digit)

	timeStart := time.Now()

	result := removeDigit(number, digit)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
