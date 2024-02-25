package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func constructArray(n int, k int) []int {
	// 4ms
	ans := make([]int, n)
	l, r := 1, n
	for i := 0; l <= r; i++ {
		if k > 1 {
			if k%2 != 0 {
				ans[i] = l
				l++
			} else {
				ans[i] = r
				r--
			}
			k--
		} else {
			ans[i] = l
			l++
		}
	}
	return ans
}

func constructArray2(n int, k int) []int {
	// 4ms
	var ans []int
	l, r := 1, n
	for l <= r {
		if k > 1 {
			if k%2 != 0 {
				ans = append(ans, l)
				l++
			} else {
				ans = append(ans, r)
				r--
			}
			k--
		} else {
			ans = append(ans, l)
			l++
		}
	}
	return ans
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	n, _ := strconv.Atoi(flds[0])
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("n = %d, k = %d\n", n, k)

	timeStart := time.Now()

	result := constructArray(n, k)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
