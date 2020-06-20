package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func getPermutation(n int, k int) string {
	// 0ms
	if n == 0 {
		return ""
	}

	mark := make([]int, n)
	mark[0] = 1
	for i := 1; i < n; i++ {
		mark[i] = (i + 1) * mark[i-1]
	}

	used := make([]bool, n)
	len := n
	resultStr := ""
	for i := 0; i < n; i++ {
		num := (k-1)/(mark[n-1-i]/len) + 1
		k = (k-1)%(mark[n-1-i]/len) + 1
		len--
		count := 0
		for j := 0; j < n; j++ {
			if used[j] {
				continue
			}
			count++
			if count == num {
				resultStr += strconv.Itoa(j + 1)
				used[j] = true
				break
			}
		}
	}
	return resultStr
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")
	n, _ := strconv.Atoi(flds[0])
	k, _ := strconv.Atoi(flds[1])

	fmt.Printf("n = %d, k = %d\n", n, k)
	timeStart := time.Now()

	result := getPermutation(n, k)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
