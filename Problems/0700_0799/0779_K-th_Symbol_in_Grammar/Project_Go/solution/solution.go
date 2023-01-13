package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func kthGrammar(n int, k int) int {
	// 0ms
	order, change := k-1, 0
	for order > 0 {
		if order%2 == 1 {
			change++
		}
		order /= 2
	}
	return change % 2
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

	result := kthGrammar(n, k)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
