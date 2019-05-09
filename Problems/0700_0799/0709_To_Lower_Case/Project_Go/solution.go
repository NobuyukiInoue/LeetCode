package main

import (
	"fmt"
	"strings"
	"time"
)

func toLowerCase(str string) string {
	tempstr := []rune(str)
	for i, _ := range tempstr {
		if 0x40 <= tempstr[i] && tempstr[i] <= 0x5a {
			tempstr[i] += 0x20
		}
	}

	return string(tempstr)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	str := strings.Replace(temp, "]", "", -1)

	fmt.Printf("str = %s\n", str)

	timeStart := time.Now()

	result := toLowerCase(str)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
