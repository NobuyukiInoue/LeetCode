package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func hasSameDigits(s string) bool {
	// 17ms - 18ms
	for len(s) > 2 {
		var new_s []string
		for i := 0; i < len(s)-1; i++ {
			new_s = append(new_s, string((s[i]-'0'+s[i+1]-'0')%10))
		}
		s = strings.Join(new_s, "")
	}
	return s[0] == s[1]
}

func hasSameDigits2(s string) bool {
	// 21ms - 22ms
	for len(s) > 2 {
		new_s := ""
		for i := 0; i < len(s)-1; i++ {
			new_s += string((s[i] - '0' + s[i+1] - '0') % 10)
		}
		s = new_s
	}
	return s[0] == s[1]
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = \"%s\"\n", s)

	timeStart := time.Now()

	result := hasSameDigits(s)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
