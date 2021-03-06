package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func compress(chars []byte) int {
	// 4ms
	for i := 0; i < len(chars)-1; i++ {
		count := 1
		c := chars[i]
		nextChar := chars[i+1]
		for c == nextChar {
			count++
			if i+count < len(chars) {
				nextChar = chars[i+count]
				continue
			}
			break
		}
		if count > 1 {
			chars = append(chars[:i+1], chars[i+count:]...)
			bts := []byte(strconv.Itoa(count))
			for n := 0; n < len(bts); n++ {
				b := bts[n]
				chars = append(chars, 0)
				copy(chars[i+1:], chars[i:])
				chars[i+1] = b
				i++
			}
		}
	}
	return len(chars)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	flds := strings.Replace(temp, ",", "", -1)
	chars := []byte(flds)

	fmt.Printf("chars = %s\n", chars)
	timeStart := time.Now()

	result := compress(chars)

	timeEnd := time.Now()

	fmt.Printf("result = %d, chars = %s\n", result, chars)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
