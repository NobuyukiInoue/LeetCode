package solution

import (
	"fmt"
	"strings"
	"time"
)

func decodeMessage(key string, message string) string {
	// 10ms
	dic := make([]byte, 26)
	i := 0
	for _, ch := range key {
		if i < 26 && ch != ' ' && dic[ch-'a'] == 0 {
			dic[ch-'a'] = byte('a' + i)
			i++
		}
	}
	res := ""
	for _, ch := range message {
		if ch == ' ' {
			res = res + " "
		} else {
			res = res + string(dic[ch-'a'])
		}
	}
	return res
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")
	key, message := flds[0], flds[1]
	fmt.Printf("key = %s, message = %s\n", key, message)

	timeStart := time.Now()

	result := decodeMessage(key, message)

	timeEnd := time.Now()

	fmt.Printf("result = \"%s\"\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
