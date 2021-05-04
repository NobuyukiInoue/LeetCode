package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func smallestRepunitDivByK(K int) int {
	// 4ms
	if K%2 == 0 || K%5 == 0 {
		return -1
	}
	num, base := 1, 1
	for num%K != 0 {
		num = (num*10 + 1) % K
		base++
	}
	return base
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	K, _ := strconv.Atoi(flds)
	fmt.Printf("K = %d\n", K)

	timeStart := time.Now()

	result := smallestRepunitDivByK(K)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
