package main

import (
	"fmt"
	"strings"
	"time"
)

func defangIPaddr(address string) string {
	return strings.Replace(address, ".", "[.]", -1)
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	address := strings.Replace(temp, "]", "", -1)

	fmt.Printf("address = %s\n", address)
	timeStart := time.Now()

	result := defangIPaddr(address)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
