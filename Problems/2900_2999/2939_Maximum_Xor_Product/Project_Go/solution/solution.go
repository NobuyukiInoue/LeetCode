package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func maximumXorProduct(a int64, b int64, n int) int {
	// 0ms
	mask := int64((1 << n) - 1)
	temp_a := a & ^mask
	temp_b := b & ^mask
	for i := n - 1; i >= 0; i-- {
		x := int64(1 << i)
		if ((a >> i) & 1) == ((b >> i) & 1) {
			temp_a |= x
			temp_b |= x
		} else {
			if temp_a > temp_b {
				temp_b |= x
			} else {
				temp_a |= x
			}
		}
	}
	MOD := int64(1_000_000_007)
	return int(((temp_a % MOD) * (temp_b % MOD)) % MOD)
}

func maximumXorProduct_bad(a int64, b int64, n int) int {
	for i := 0; i < n; i++ {
		x := int64(1) << i
		t1, t2 := a^x, b^x
		if t1*t2 > a*b {
			a = t1
			b = t2
		}
	}
	MOD := int64(1_000_000_007)
	ans := ((a % MOD) * (b % MOD)) % MOD
	return int(ans)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")
	i_a, _ := strconv.Atoi(flds[0])
	i_b, _ := strconv.Atoi(flds[1])
	a, b := int64(i_a), int64(i_b)
	n, _ := strconv.Atoi(flds[2])

	fmt.Printf("a = %d, b = %d, n = %d\n", a, b, n)

	timeStart := time.Now()

	result := maximumXorProduct(a, b, n)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
