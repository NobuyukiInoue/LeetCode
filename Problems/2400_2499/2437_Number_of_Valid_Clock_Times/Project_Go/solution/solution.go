package solution

import (
	"fmt"
	"strings"
	"time"
)

func countTime(time string) int {
	// 0ms - 1ms
	res := 1
	if time[0] == '?' {
		if time[1] == '?' {
			res = 24
		} else if time[1] < '4' {
			res = 3
		} else {
			res = 2
		}
	} else if time[1] == '?' {
		if time[0] < '2' {
			res = 10
		} else {
			res = 4
		}
	}

	if time[3] == '?' {
		res *= 6
	}
	if time[4] == '?' {
		res *= 10
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	v_time := strings.Replace(temp, "]", "", -1)
	fmt.Printf("time = %s\n", v_time)

	timeStart := time.Now()

	result := countTime(v_time)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
