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

func str2IntArray(flds string) []int {
	numsStr := strings.Split(flds, ",")
	nums := make([]int, len(numsStr))

	for i := 0; i < len(nums); i++ {
		nums[i], _ = strconv.Atoi(numsStr[i])
	}

	return nums
}

func intArray2string(arr []int) string {
	if len(arr) <= 0 {
		return ""
	}

	resultStr := "["
	for i := 0; i < len(arr); i++ {
		if i > 0 {
			resultStr += ","
		}
		resultStr += strconv.Itoa(arr[i])
	}

	return resultStr + "]"
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	n, _ := strconv.Atoi(flds[0])
	primes := str2IntArray(flds[1])

	fmt.Printf("n = %d\n", n)
	fmt.Printf("primes = %s\n", intArray2string(primes))

	timeStart := time.Now()

	result := nthSuperUglyNumber(n, primes)

	fmt.Printf("result = %d\n", result)

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
