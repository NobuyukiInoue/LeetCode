package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func passThePillow(n int, time int) int {
	// 1ms
	return n - myAbs(n-1-time%(n*2-2))
}

func myAbs(n int) int {
	if n >= 0 {
		return n
	}
	return -n
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	n, _ := strconv.Atoi(flds[0])
	v_time, _ := strconv.Atoi(flds[1])
	fmt.Printf("n = %d, time = %d\n", n, v_time)

	timeStart := time.Now()

	result := passThePillow(n, v_time)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
