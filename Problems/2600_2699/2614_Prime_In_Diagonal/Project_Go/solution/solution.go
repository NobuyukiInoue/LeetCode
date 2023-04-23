package solution

import (
	"fmt"
	"math"
	"sort"
	"strings"
	"time"
)

func diagonalPrime(nums [][]int) int {
	// 103ms - 106ms
	var diagonals []int
	for i, num := range nums {
		if i != -(i + 1) {
			diagonals = append(diagonals, num[i], num[len(num)-(i+1)])
		} else {
			diagonals = append(diagonals, num[i])
		}
	}
	sort.Sort(sort.IntSlice(diagonals))
	for i := len(diagonals) - 1; i >= 0; i-- {
		if isPrime(diagonals[i]) {
			return diagonals[i]
		}
	}
	return 0
}

func isPrime(n int) bool {
	if n == 1 {
		return false
	}
	if n == 2 || n == 3 {
		return true
	}
	if n%2 == 0 || n%3 == 0 {
		return false
	}
	limit := int(math.Sqrt(float64(n)))
	for i := 5; limit-i >= 0; i += 2 {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	flds := strings.Replace(temp, "]]", "", -1)

	str_mat := strings.Split(flds, "],[")
	nums := make([][]int, len(str_mat))
	for i := 0; i < len(str_mat); i++ {
		nums[i] = StringToIntArray(str_mat[i])
	}
	fmt.Printf("nums = %s\n", IntIntArrayToGridString(nums))

	timeStart := time.Now()

	result := diagonalPrime(nums)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
