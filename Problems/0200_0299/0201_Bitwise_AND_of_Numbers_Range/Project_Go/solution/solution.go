package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func rangeBitwiseAnd(m int, n int) int {
	// 8ms
	if m == 0 {
		return 0
	}

    shift := uint(0)
	for m != n {
		m >>= 1
		n >>= 1
		shift += 1
	}

	return m << shift
}

func rangeBitwiseAnd2(m int, n int) int {
	// 8ms
    diff := n-m
    bit := uint(0)
    for diff != 0 {
        diff = diff >> 1
        bit++
    }
    return (m >> bit << bit) & (n >> bit << bit)
}


func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	m, _ := strconv.Atoi(flds[0])
	n, _ := strconv.Atoi(flds[1])
	fmt.Printf("m = %d, n = %d\n", m, n)

	timeStart := time.Now()

	result := rangeBitwiseAnd(m, n)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
