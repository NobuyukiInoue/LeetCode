package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"

	"./hashset"
)

func Hash_Main(ope []string, para []string) {
	if len(ope) != len(para) {
		return
	}

	if len(ope) <= 0 || len(para) <= 0 {
		return
	}

	mh := new(hashset.MyHashSet)

	for i, _ := range ope {
		// fmt.Printf("ope[%d] = %s, para[%d] = %s\n", i, ope[i], i, para[i])
		if ope[i] == "MyHashSet" {

		} else if ope[i] == "add" {
			data, _ := strconv.Atoi(para[i])
			mh.Add(data)
			fmt.Printf("Add[%d]\n", data)

		} else if ope[i] == "remove" {
			data, _ := strconv.Atoi(para[i])
			mh.Remove(data)
			fmt.Printf("Remove[%d]\n", data)

		} else if ope[i] == "contains" {
			data, _ := strconv.Atoi(para[i])
			result := mh.Contains(data)
			fmt.Printf("Contains[%d] = %s\n", data, strconv.FormatBool(result))
		}
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[[", "", -1)
	temp = strings.Replace(temp, "]]]", "", -1)

	flds := strings.Split(temp, "]],[[")
	ope := strings.Split(flds[0], ",")

	temp_flds1 := strings.Replace(flds[1], "[", "", -1)
	temp_flds1 = strings.Replace(temp_flds1, "]", "", -1)
	para := strings.Split(temp_flds1, ",")

	fmt.Printf("ope = %s\n", ope)
	fmt.Printf("para = %s\n", para)

	timeStart := time.Now()

	Hash_Main(ope, para)

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
