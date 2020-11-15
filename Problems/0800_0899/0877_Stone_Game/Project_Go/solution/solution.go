package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func stoneGame(piles []int) bool {
	if len(piles)%2 == 0 {
		return true
	}
	return false
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	piles := StringToIntArray(flds)
	fmt.Printf("piles = [%s]\n", IntArrayToString(piles))

	timeStart := time.Now()

	result := stoneGame(piles)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
