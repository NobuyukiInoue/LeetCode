package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func kthFactor(n int, k int) int {
	// 0ms
	cnt := 0
	for i := 1; i < n/2+1; i++ {
		if n%i == 0 {
			cnt++
			if cnt == k {
				return i
			}
		}
	}
	if cnt == k-1 {
		return n
	}
	return -1
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

	result := kthFactor(n, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
