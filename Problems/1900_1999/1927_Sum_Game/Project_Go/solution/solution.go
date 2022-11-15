package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func sumGame(num string) bool {
	// 20ms - 24ms
	len_num, res := len(num), 0.0
	var res1 float64
	for i, _ := range num {
		if i < len_num/2 {
			res1 = 1
		} else {
			res1 = -1
		}
		if num[i] == '?' {
			res += res1 * 4.5
		} else {
			res += res1 * float64(num[i]-'0')
		}
	}
	return res != 0
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	num := strings.Replace(temp, "]", "", -1)
	fmt.Printf("num = %s\n", num)

	timeStart := time.Now()

	result := sumGame(num)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
