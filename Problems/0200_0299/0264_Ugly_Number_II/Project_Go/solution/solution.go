package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func nthUglyNumber(n int) int {
	// 0ms
	ugly := make([]int, n)
	for i := 0; i < len(ugly); i++ {
		ugly[i] = 1
	}

	i2, i3, i5 := -1, -1, -1
	x, v2, v3, v5 := 1, 1, 1, 1

	for k := 0; k < n; k++ {
		x = Min(v2, v3, v5)
		ugly[k] = x
		if x == v2 {
			i2++
			v2 = ugly[i2] * 2
		}
		if x == v3 {
			i3++
			v3 = ugly[i3] * 3
		}
		if x == v5 {
			i5++
			v5 = ugly[i5] * 5
		}
	}
	return x
}

func Min(a int, b int, c int) int {
	if a <= b && a <= c {
		return a
	} else if b <= a && b <= c {
		return b
	} else {
		return c
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	fld := strings.Replace(temp, "]", "", -1)
	n, _ := strconv.Atoi(fld)

	fmt.Printf("n = %d\n", n)
	timeStart := time.Now()

	result := nthUglyNumber(n)
	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
