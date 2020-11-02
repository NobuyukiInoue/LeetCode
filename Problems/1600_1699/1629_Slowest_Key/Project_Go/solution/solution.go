package solution

import (
	"fmt"
	"strings"
	"time"
)

func slowestKey(releaseTimes []int, keysPressed string) byte {
	// 4ms
	maxDiff := releaseTimes[0]
	result := keysPressed[0]
	for i := 1; i < len(releaseTimes); i++ {
		diff := releaseTimes[i] - releaseTimes[i - 1]
		if diff >= maxDiff {
			currChar := keysPressed[i]
			if diff > maxDiff || currChar > result {
				result = currChar
			}
			maxDiff = diff
		}
	}
	return result
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)

	flds := strings.Split(temp, "],[")
	releaseTimes := StringToIntArray(strings.Replace(flds[0], "[[", "", -1))
	keysPressed := strings.Replace(flds[1], "]]", "", -1)

	fmt.Printf("releaseTimes[] = %s\n", IntArrayToString(releaseTimes))
	fmt.Printf("keysPressed = %s\n", keysPressed)

	timeStart := time.Now()

	result := slowestKey(releaseTimes, keysPressed)

	timeEnd := time.Now()
	fmt.Printf("res =  %c\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
