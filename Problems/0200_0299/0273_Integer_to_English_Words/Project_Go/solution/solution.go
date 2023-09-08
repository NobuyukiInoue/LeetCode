package solution

import (
	"fmt"
	"math"
	"strconv"
	"strings"
	"time"
)

// 0ms
var ones []string = []string{"", " One", " Two", " Three", " Four", " Five", " Six", " Seven", " Eight", " Nine", " Ten", " Eleven", " Twelve", " Thirteen", " Fourteen", " Fifteen", " Sixteen", " Seventeen", " Eighteen", " Nineteen"}
var tens []string = []string{"", " Ten", " Twenty", " Thirty", " Forty", " Fifty", " Sixty", " Seventy", " Eighty", " Ninety"}
var thousands []string = []string{"", " Thousand", " Million", " Billion"}

func numberToWords(num int) string {
	if num == 0 {
		return "Zero"
	}
	return helper(num)[1:]
}

func helper(n int) string {
	if n < 20 {
		return ones[n]
	}
	if n < 100 {
		return tens[n/10] + helper(n%10)
	}
	if n < 1000 {
		return helper(n/100) + " Hundred" + helper(n%100)
	}
	for i := 3; i >= 0; i-- {
		if n >= int(math.Pow(float64(1000), float64(i))) {
			return helper(n/int(math.Pow(float64(1000), float64(i)))) + thousands[i] + helper(n%int(math.Pow(float64(1000), float64(i))))
		}
	}
	return ""
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	fld := strings.Replace(temp, "]", "", -1)
	num, _ := strconv.Atoi(fld)
	fmt.Printf("num = %d\n", num)

	timeStart := time.Now()

	result := numberToWords(num)

	timeEnd := time.Now()

	fmt.Printf("result = \"%s\"\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
