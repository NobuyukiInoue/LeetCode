package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func getHint(secret string, guess string) string {
	// 0ms
	a, b := 0, 0
	digits := make([]int, 10)
	for i := 0; i < len(secret); i++ {
		if secret[i] == guess[i] {
			a++
		} else {
			digits[secret[i]-'0']++
			if digits[secret[i]-'0'] <= 0 {
				b++
			}
			digits[guess[i]-'0']--
			if digits[guess[i]-'0'] >= 0 {
				b++
			}
		}
	}
	return strconv.Itoa(a) + "A" + strconv.Itoa(b) + "B"
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	flds := strings.Split(temp, ",")

	secret := flds[0]
	guess := flds[1]

	fmt.Printf("secret = %s, guess = %s\n", secret, guess)

	timeStart := time.Now()

	result := getHint(secret, guess)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
