package solution

import (
	"fmt"
	"strings"
	"time"
)

func pushDominoes(dominoes string) string {
	// 4ms
	dominoes = "L" + dominoes + "R"
	res := make([]byte, 0)
	left := 0
	for right := 1; right < len(dominoes); right++ {
		if dominoes[right] == '.' {
			continue
		}
		middle := right - left - 1
		if left > 0 {
			res = append(res, dominoes[left])
		}
		if dominoes[left] == dominoes[right] {
			for count := 0; count < middle; count++ {
				res = append(res, dominoes[left])
			}
		} else if dominoes[left] == 'L' && dominoes[right] == 'R' {
			for count := 0; count < middle; count++ {
				res = append(res, '.')
			}
		} else {
			for count := 0; count < middle/2; count++ {
				res = append(res, 'R')
			}
			for count := 0; count < middle%2; count++ {
				res = append(res, '.')
			}
			for count := 0; count < middle/2; count++ {
				res = append(res, 'L')
			}
		}
		left = right
	}
	return string(res)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	dominoes := strings.Replace(temp, "]", "", -1)
	fmt.Printf("dominoes = %s\n", dominoes)

	timeStart := time.Now()

	result := pushDominoes(dominoes)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
