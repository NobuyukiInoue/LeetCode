package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func validateStackSequences(pushed []int, popped []int) bool {
	// 4ms
	stack := make([]int, 0)
	i := 0
	for _, x := range pushed {
		stack = append(stack, x)
		for len(stack) > 0 && stack[len(stack)-1] == popped[i] {
			i++
			stack = stack[:len(stack)-1]
		}
	}
	return len(stack) == 0
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	pushed := StringToIntArray(flds[0])
	popped := StringToIntArray(flds[1])
	fmt.Printf("pushed = %s\n", IntArrayToString(pushed))
	fmt.Printf("popped = %s\n", IntArrayToString(popped))

	timeStart := time.Now()

	result := validateStackSequences(pushed, popped)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
