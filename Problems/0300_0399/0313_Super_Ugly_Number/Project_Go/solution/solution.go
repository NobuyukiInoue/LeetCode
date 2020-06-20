package solution

import (
	"fmt"
	"math"
	"strconv"
	"strings"
	"time"
)

func nthSuperUglyNumber(n int, primes []int) int {
	// 8ms
	idx := make([]int, len(primes))
	nums := make([]int, n)
	nums[0] = 1
	ctr := 1
	for ctr < n {
		min := math.MaxInt32
		for i := 0; i < len(primes); i++ {
			t := nums[idx[i]] * primes[i]
			if t <= nums[ctr-1] {
				idx[i]++
				t = nums[idx[i]] * primes[i]
			}
			min = Min(min, t)
		}
		nums[ctr] = min
		ctr++
	}
	return nums[n-1]
}

func Min(a int, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	n, _ := strconv.Atoi(flds[0])
	primes := StringToIntArray(flds[1])

	fmt.Printf("n = %d\n", n)
	fmt.Printf("primes = [%s]\n", IntArrayToString(primes))

	timeStart := time.Now()

	result := nthSuperUglyNumber(n, primes)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
