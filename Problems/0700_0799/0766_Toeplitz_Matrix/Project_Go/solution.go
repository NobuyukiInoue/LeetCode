package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func isToeplitzMatrix(matrix [][]int) bool {
	for i := 0; i < len(matrix)-1; i++ {
		for j := 0; j < len(matrix[i])-1; j++ {
			if matrix[i][j] != matrix[i+1][j+1] {
				return false
			}
		}
	}

	return true
}

func IntArray2string(arr []int) string {
	if len(arr) <= 0 {
		return ""
	}

	resultStr := "["
	for i := 0; i < len(arr); i++ {
		if i > 0 {
			resultStr += ","
		}
		resultStr += strconv.Itoa(arr[i])
	}

	return resultStr + "]"
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	matrix := make([][]int, len(flds))
	for i, _ := range flds {
		line := strings.Split(flds[i], ",")
		//	fmt.Printf("line = %s\n", line)
		matrix[i] = make([]int, len(line))
		for j, _ := range line {
			matrix[i][j], _ = strconv.Atoi(line[j])
		}
		fmt.Printf("matrix = %s\n", IntArray2string(matrix[i]))
	}

	timeStart := time.Now()

	result := isToeplitzMatrix(matrix)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
