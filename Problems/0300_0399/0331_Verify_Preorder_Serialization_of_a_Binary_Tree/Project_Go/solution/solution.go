package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func isValidSerialization(preorder string) bool {
	// 0ms
	need := 1
	for _, val := range strings.Split(preorder, ",") {
		if need == 0 {
			return false
		}
		if strings.Index(val, "#") >= 0 {
			need--
		} else {
			need++
		}
	}
	return need == 0
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	preorder := strings.Replace(temp, "]", "", -1)
	fmt.Printf("preorder = %s\n", preorder)

	timeStart := time.Now()

	result := isValidSerialization(preorder)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
