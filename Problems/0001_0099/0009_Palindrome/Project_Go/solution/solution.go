package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func isPalindrome(x int) bool {
	// 12ms
	temp := strconv.Itoa(x)
	tempLength := len(temp)

	for i := 0; i < tempLength / 2; i++ {
		if temp[i] != temp[tempLength - 1 - i] {
			return false
		}
	}

	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	fld := strings.Replace(temp, "]", "", -1)

	x, _ := strconv.Atoi(fld)
	fmt.Printf("x = %d\n", x)

	timeStart := time.Now()

	result := isPalindrome(x)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
