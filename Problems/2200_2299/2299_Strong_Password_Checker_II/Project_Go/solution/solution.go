package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func strongPasswordCheckerII(password string) bool {
	// 0ms - 2ms
	seen := make(map[rune]int)
	for i := 0; i < len(password); i++ {
		if i > 0 && password[i] == password[i-1] {
			return false
		}
		if 'a' <= password[i] && password[i] <= 'z' {
			seen['l']++
		} else if 'A' <= password[i] && password[i] <= 'Z' {
			seen['u']++
		} else if '0' <= password[i] && password[i] <= '9' {
			seen['d']++
		} else if strings.Contains("!@#$%^&*()-+", string(password[i])) {
			seen['s']++
		}
	}
	return len(password) >= 8 && len(seen) == 4
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	password := strings.Replace(temp, "]", "", -1)
	fmt.Printf("password = %s\n", password)

	timeStart := time.Now()

	result := strongPasswordCheckerII(password)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
