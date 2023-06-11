package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func decodeAtIndex(s string, k int) string {
	// 1ms - 2ms
	var i int
	tape_length := int64(0)
	k2 := int64(k)
	for i = 0; tape_length < k2; i++ {
		if '0' <= s[i] && s[i] <= '9' {
			tape_length *= int64(s[i] - '0')
		} else {
			tape_length++
		}
	}
	i--
	for ; i > 0; i-- {
		if '0' <= s[i] && s[i] <= '9' {
			tape_length /= int64(s[i] - '0')
			k2 %= tape_length
		} else {
			if k2 == tape_length || k2 == 0 {
				break
			}
			tape_length--
		}
	}
	return string(s[i])
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	s := flds[0]
	k, _ := strconv.Atoi(flds[1])
	fmt.Printf("s = %s, k = %d\n", s, k)

	timeStart := time.Now()

	result := decodeAtIndex(s, k)

	timeEnd := time.Now()

	fmt.Printf("result = \"%s\"\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
