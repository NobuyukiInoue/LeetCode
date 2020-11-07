package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func isNumber(s string) bool {
	// 0ms
	s = strings.TrimSpace(s)

	pointSeen := false
	eSeen := false
	numberSeen := false
	numberAfterE := true
	for i := 0; i < len(s); i++ {
		if '0' <= s[i] && s[i] <= '9' {
			numberSeen = true
			numberAfterE = true
		} else if s[i] == '.' {
			if eSeen || pointSeen {
				return false
			}
			pointSeen = true
		} else if s[i] == 'e' {
			if eSeen || !numberSeen {
				return false
			}
			numberAfterE = false
			eSeen = true
		} else if s[i] == '-' || s[i] == '+' {
			if i != 0 && s[i-1] != 'e' {
				return false
			}
		} else {
			return false
		}
	}

	return numberSeen && numberAfterE
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := isNumber(s)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
