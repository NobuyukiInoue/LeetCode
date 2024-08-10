package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func minChanges(n int, k int) int {
	// 0ms - 4ms
	ans := 0
	for n > 0 || k > 0 {
		m_n, m_k := n%2, k%2
		if m_n == 1 && m_k == 0 {
			ans++
		}
		if m_n == 0 && m_k == 1 {
			return -1
		}
		n /= 2
		k /= 2
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

	result := minChanges(n, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Enecute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
