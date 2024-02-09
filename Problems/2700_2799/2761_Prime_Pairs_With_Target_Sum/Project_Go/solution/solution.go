package solution

import (
	"fmt"
	"math"
	"strconv"
	"strings"
	"time"
)

func findPrimePairs(n int) [][]int {
	// 97ms - 99ms
	lst := make([]bool, n+1)
	for i := 2; i < int(math.Sqrt(float64(n)))+1; i++ {
		if !lst[i] {
			for j := i * 2; j < n+1; j += i {
				lst[j] = true
			}
		}
	}
	var ans [][]int
	for i := 2; i < n/2+1; i++ {
		x, y := i, n-i
		if !lst[x] && !lst[y] && x <= y {
			ans = append(ans, []int{x, y})
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	fld := strings.Replace(temp, "]", "", -1)
	n, _ := strconv.Atoi(fld)
	fmt.Printf("n = %d\n", n)

	timeStart := time.Now()

	result := findPrimePairs(n)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", IntIntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
