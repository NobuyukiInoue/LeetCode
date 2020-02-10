package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func removeKdigits(num string, k int) string {
	// 0ms
	remain := len(num) - k
	numArray := []rune(num)
	res := make([]rune, remain)
	index := 0
	for i := 0; i < len(numArray); i++ {
		for (len(numArray)-i > remain-index) && (index > 0 && numArray[i] < res[index-1]) {
			index--
		}
		if index < remain {
			res[index] = numArray[i]
			index++
		}
	}

	index = 0
	for index < remain {
		if res[index] != '0' {
			break
		}
		index++
	}

	s := string(res[index:])

	if len(s) == 0 {
		return "0"
	}
	return s
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	num := flds[0]
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("num = %s, k = %d\n", num, k)

	timeStart := time.Now()

	result := removeKdigits(num, k)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
