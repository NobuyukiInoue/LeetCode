package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func xorOperation(n int, start int) int {
	// 0ms
	res := start
	for i := 1; i < n; i++ {
    	res ^= start + 2*i
    }
    return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)

	flds := strings.Split(temp, "],[")
	n, _ := strconv.Atoi(flds[0])
	start, _ := strconv.Atoi(flds[1])

	fmt.Printf("n = %d, start = %d\n", n, start)

	timeStart := time.Now()

	result := xorOperation(n, start)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
