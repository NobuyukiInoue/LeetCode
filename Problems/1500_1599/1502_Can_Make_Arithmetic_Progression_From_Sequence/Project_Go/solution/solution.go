package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"time"
)

func canMakeArithmeticProgression(arr []int) bool {
	// 2ms
	sort.Sort(sort.IntSlice(arr))
	dif := arr[1] - arr[0]
	for i := 2; i < len(arr); i++ {
		if arr[i] - arr[i - 1] != dif {
			return false;
		}
	}
	return true;
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	flds := strings.Replace(temp, "]", "", -1)

	arr := StringToIntArray(flds)
	fmt.Printf("arr = [%s]\n", IntArrayToString(arr))

	timeStart := time.Now()

	result := canMakeArithmeticProgression(arr)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
