package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func largeGroupPositions(S string) [][]int {
	res := make([][]int, 0)
	start := 0
	length := 1
	data := []byte(S)
	curr := data[0]
	if len(data) < 3 {
		return res
	}
	for i := 1; i < len(data); i++ {
		if data[i] == curr {
			length++
		} else {
			if length >= 3 {
				tmp := make([]int, 2)
				tmp[0] = start
				tmp[1] = i - 1
				res = append(res, tmp)
			}
			curr = data[i]
			length = 1
			start = i
		}
	}
	if length >= 3 {
		tmp := make([]int, 2)
		tmp[0] = start
		tmp[1] = len(data) - 1
		res = append(res, tmp)
	}
	return res
}

func ArrayInt_to_String(list [][]int) string {
	if len(list) <= 0 {
		return ""
	}

	resultStr := "["
	for i := 0; i < len(list); i++ {
		if i > 0 {
			resultStr += ","
		}

		resultStr += "["
		for j := 0; j < len(list[i]); j++ {
			if j > 0 {
				resultStr += ","
			}

			resultStr += strconv.Itoa(list[i][j])
		}
		resultStr += "]"
	}
	resultStr += "]"

	return resultStr
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	S := strings.Replace(temp, "]", "", -1)

	fmt.Printf("S = %s\n", S)

	timeStart := time.Now()

	result := largeGroupPositions(S)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", ArrayInt_to_String(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
