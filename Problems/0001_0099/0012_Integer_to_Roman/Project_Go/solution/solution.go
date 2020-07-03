package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func intToRoman(num int) string {
	// 4ms
    values := []int{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1}
	romans := []string{"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"}
	result := ""
	i := 0
	for num > 0 {
		for values[i] > num {
			i++
		}
		num -= values[i]
		result += romans[i]
	}
	return result
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	fld := strings.Replace(temp, "]", "", -1)

	nums, _ := strconv.Atoi(fld);
	fmt.Printf("nums = %d\n", nums)

	timeStart := time.Now()

	result := intToRoman(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
