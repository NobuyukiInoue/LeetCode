package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"

	"./numarray"
)

func NumArrayMain(ope []string, para []string) {
	if len(ope) != len(para) {
		return
	}

	if len(ope) <= 0 || len(para) <= 0 {
		return
	}

	nums_str := strings.Split(para[0], ",")
	fmt.Printf("nums_str = %s\n", nums_str)

	nums := make([]int, len(nums_str))
	for i, _ := range nums {
		nums[i], _ = strconv.Atoi(nums_str[i])
	}

	//nm := new(numarray.NumArray)
	nm := numarray.Constructor(nums)

	for i, _ := range ope {
		if ope[i] == "NumArray" {

		} else if ope[i] == "update" {
			flds := strings.Split(para[i], ",")
			i, _ := strconv.Atoi(flds[0])
			val, _ := strconv.Atoi(flds[1])
			nm.Update(i, val)
			fmt.Printf("update(%d, %d)\n", i, val)
		} else if ope[i] == "sumRange" {
			flds := strings.Split(para[i], ",")
			i, _ := strconv.Atoi(flds[0])
			j, _ := strconv.Atoi(flds[1])
			sum := nm.SumRange(i, j)
			fmt.Printf("sumRange(%d, %d) = %d\n", i, j, sum)
		}
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	flds := strings.Split(temp, "],[[[")

	flds0 := strings.Replace(flds[0], "[", "", -1)
	flds0 = strings.Replace(flds0, "[", "", -1)
	flds0 = strings.Replace(flds0, "]", "", -1)
	ope := strings.Split(flds0, ",")

	var para []string
	if len(flds) > 1 {
		params := strings.Split(flds[1], "]],[")
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

	NumArrayMain(ope, para)

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
