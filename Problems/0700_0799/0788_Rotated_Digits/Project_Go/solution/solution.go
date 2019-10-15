package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func rotatedDigits(N int) int {
	// 4ms
	count := 0
	for num := 0; num <= N; num++ {
		number := strconv.Itoa(num)
		if strings.ContainsAny(number, "3") || strings.ContainsAny(number, "7") || strings.ContainsAny(number, "4") {
			continue
		}
		if strings.ContainsAny(number, "2") || strings.ContainsAny(number, "5") || strings.ContainsAny(number, "6") || strings.ContainsAny(number, "9") {
			count++
		}
	}

	return count
}

func rotatedDigits2(N int) int {
	// 8ms
	count := 0
	for num := 0; num <= N; num++ {
		number := strconv.Itoa(num)
		if strings.Index(number, "3") >= 0 || strings.Index(number, "7") >= 0 || strings.Index(number, "4") >= 0 {
			continue
		}
		if strings.Index(number, "2") >= 0 || strings.Index(number, "5") >= 0 || strings.Index(number, "6") >= 0 || strings.Index(number, "9") >= 0 {
			count++
		}
	}

	return count
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	N, _ := strconv.Atoi(flds)

	fmt.Printf("N = %d\n", N)

	timeStart := time.Now()

	result := rotatedDigits(N)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
