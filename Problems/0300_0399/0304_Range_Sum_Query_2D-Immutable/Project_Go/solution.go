package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"

	"./nummatrix"
)

func NumMatrixMain(ope []string, para []string) {
	if len(ope) != len(para) {
		return
	}

	if len(ope) <= 0 || len(para) <= 0 {
		return
	}

	temp_str := strings.Replace(para[0], "[[", "", -1)
	temp_str = strings.Replace(temp_str, "]]", "", -1)
	matrix_str := strings.Split(temp_str, "],[")

	matrix := make([][]int, len(matrix_str))
	for i, _ := range matrix {
		cols := strings.Split(matrix_str[i], ",")
		matrix[i] = make([]int, len(cols))
		for j, _ := range cols {
			matrix[i][j], _ = strconv.Atoi(cols[j])
		}
	}

	//nm := new(nummatrix.NumMatrix)
	nm := nummatrix.Constructor(matrix)
	nm.PrintMatrix()

	for i, _ := range ope {
		if ope[i] == "NumMatrix" {

		} else if ope[i] == "sumRegion" {
			flds := strings.Split(para[i], ",")
			row1, _ := strconv.Atoi(flds[0])
			col1, _ := strconv.Atoi(flds[1])
			row2, _ := strconv.Atoi(flds[2])
			col2, _ := strconv.Atoi(flds[3])
			sum := nm.SumRegion(row1, col1, row2, col2)
			fmt.Printf("sumRegion(%d, %d, %d, %d) = %d\n", row1, col1, row2, col2, sum)
		}
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	flds := strings.Split(temp, "],[[[[")

	flds0 := strings.Replace(flds[0], "[", "", -1)
	flds0 = strings.Replace(flds0, "[", "", -1)
	flds0 = strings.Replace(flds0, "]", "", -1)
	ope := strings.Split(flds0, ",")

	var para []string
	if len(flds) > 1 {
		params := strings.Split(flds[1], "]]],[")
		paras_str := strings.Replace(params[1], "]]]", "", -1)
		paras_str2 := strings.Split(paras_str, "],[")

		para = make([]string, 1+len(paras_str2))
		para[0] = params[0]
		for i, _ := range paras_str2 {
			data := strings.Replace(paras_str2[i], "[", "", -1)
			data = strings.Replace(paras_str2[i], "]", "", -1)
			para[i+1] = data
		}
	} else {
		para = make([]string, 0)
	}

	fmt.Printf("ope = %s\n", ope)
	fmt.Printf("para = %s\n", para)

	timeStart := time.Now()

	NumMatrixMain(ope, para)

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
