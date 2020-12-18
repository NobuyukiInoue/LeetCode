package solution

import (
	"fmt"
	"strings"
	"time"
)

func interpret(command string) string {
	// 0ms
	return strings.Replace(strings.Replace(command, "()", "o", -1), "(al)", "al", -1)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	command := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = %s\n", command)

	timeStart := time.Now()

	result := interpret(command)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
