package solution

import (
	"fmt"
	"strings"
	"time"
)

func numUniqueEmails(emails []string) int {
	mp := make(map[string]int)

	for i := 0; i < len(emails); i++ {
		em := []byte(emails[i])
		k := 0
		findDot := 0
		findPlus := false
		for _, val := range emails[i] {
			if val == '@' {
				findPlus = false
				findDot++
			}
			if val == '.' || findPlus {
				if findDot == 0 {
					continue
				}
			}
			if val == '+' {
				findPlus = true
				continue
			}

			em[k] = byte(val)
			k++
		}
		if k > 0 && findDot == 1 {
			mp[string(em)[0:k]]++
		}
	}

	return len(mp)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[", "", -1)
	temp = strings.Replace(temp, "]", "", -1)
	emails := strings.Split(temp, ",")

	fmt.Printf("emails = %s\n", emails)

	timeStart := time.Now()

	result := numUniqueEmails(emails)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
