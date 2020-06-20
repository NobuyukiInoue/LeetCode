package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func isOneBitCharacter(bits []int) bool {
	i, n := 0, len(bits)-1
	for i < n {
		if bits[i] == 1 {
			i += 2
		} else {
			i++
		}
	}

	if i == n && bits[i] == 0 {
		return true
	} else {
		return false
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	bits := StringToIntArray(flds)
	fmt.Printf("bits = [%s]\n", IntArrayToString(bits))

	timeStart := time.Now()

	result := isOneBitCharacter(bits)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
