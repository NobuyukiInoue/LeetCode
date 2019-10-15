package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func findNthDigit(n int) int {
	if n < 0 {
		return 0
	}

	up_bound := 9
	i := 1
	for n > up_bound {
		i++
		up_bound += i * 9 * IntPow(10, i-1)
	}

	low_bound := up_bound - i*9*IntPow(10, i-1)
	// now i is the number of digits of this number num

	num := IntPow(10, i-1) + (n-1-low_bound)/i
	nth := (n - 1 - low_bound) % i

	return (num / IntPow(10, i-1-nth)) % 10
}

func IntPow(x int, y int) int {
	result := 1
	for count := 0; count < y; count++ {
		result *= x
	}

	return result
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	n, _ := strconv.Atoi(temp)

	fmt.Printf("n = %d\n", n)

	timeStart := time.Now()

	result := findNthDigit(n)
	fmt.Printf("result = %d\n", result)

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
