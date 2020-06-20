package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func uniqueOccurrences(arr []int) bool {
	d := make(map[int]int)
	for i := 0; i < len(arr); i++ {
		d[arr[i]]++
	}

	var s = make(map[int]int)
	for _, value := range d {
		_, exists := s[value]
		if exists {
			return false
		}
		s[value] = 1
	}
	return true
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

	result := uniqueOccurrences(arr)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
