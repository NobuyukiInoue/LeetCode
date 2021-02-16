package solution

import (
	"fmt"
	"strings"
	"time"
)

func maximumTime(vartime string) string {
	// 0ms
	res := []rune(vartime);

	if res[0] == '?' {
		if res[1] <= '3' || res[1] == '?' {
			res[0] = '2'
		} else {
			res[0] = '1'
		}
	}

	if res[1] == '?' {
		if res[0] == '2' {
			res[1] = '3'
		} else {
			res[1] = '9'
		}
	}

	if res[3] == '?' {
		res[3] = '5'
	}

	if res[4] == '?' {
		res[4] = '9'
	}

	return string(res)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	vartime := strings.Replace(temp, "]", "", -1)
	fmt.Printf("time = %s\n", vartime)

	timeStart := time.Now()

	result := maximumTime(vartime)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
