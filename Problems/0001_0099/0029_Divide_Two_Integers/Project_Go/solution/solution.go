package solution

import (
	"fmt"
	"math"
	"strconv"
	"strings"
	"time"
)

func divide(dividend int, divisor int) int {
	// 0ms - 3ms
	if divisor == 0 {
		return 0
	}
	if myAbs64(int64(dividend)) > math.MaxInt32 && divisor == -1 {
		return math.MaxInt32
	}
	quotient := 0
	negative := (dividend < 0) != (divisor < 0)
	longDividend := myAbs64(int64(dividend))
	longDivisor := myAbs64(int64(divisor))
	for longDividend >= longDivisor {
		shift := 0
		for longDividend >= (longDivisor << shift) {
			shift++
		}
		shift--
		longDividend -= longDivisor << shift
		quotient += 1 << shift
	}
	if negative {
		return -quotient
	}
	return quotient
}

func myAbs64(n int64) int64 {
	if n >= 0 {
		return n
	}
	return -n
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	dividend, _ := strconv.Atoi(flds[0])
	divisor, _ := strconv.Atoi(flds[1])
	fmt.Printf("dividend = %d, divisor = %d\n", dividend, divisor)

	timeStart := time.Now()

	result := divide(dividend, divisor)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
