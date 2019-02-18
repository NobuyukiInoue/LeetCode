package main

import "./mylinkedlist"

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func Hash_Main(ope []string, para []string) {
	if len(ope) != len(para) {
		return
	}

	if len(ope) <= 0 || len(para) <= 0 {
		return
	}

	mh := new(mylinkedlist.MyLinkedList)

	for i, _ := range ope {
		// fmt.Printf("ope[%d] = %s, para[%d] = %s\n", i, ope[i], i, para[i])
		if ope[i] == "MyLinkedList" {

		} else if ope[i] == "get" {
			key, _ := strconv.Atoi(para[i])
			result := mh.Get(key)
			fmt.Printf("get[%s] = %d\n", para[i], result)

		} else if ope[i] == "addAtHead" {
			value, _ := strconv.Atoi(para[i])
			mh.AddAtHead(value)
			fmt.Printf("addAtHead(%s)\n", para[i])

		} else if ope[i] == "addAtTail" {
			value, _ := strconv.Atoi(para[i])
			mh.AddAtTail(value)
			fmt.Printf("addAtTail(%s)\n", para[i])

		} else if ope[i] == "addAtIndex" {
			flds := strings.Split(para[i], ",")
			index, _ := strconv.Atoi(flds[0])
			value, _ := strconv.Atoi(flds[1])
			mh.AddAtIndex(index, value)
			fmt.Printf("addAtIndex(%s)\n", para[i])

		} else if ope[i] == "deleteAtIndex" {
			data, _ := strconv.Atoi(para[i])
			mh.DeleteAtIndex(data)
			fmt.Printf("Remove[%s]\n", para[i])

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

	para := strings.Split(flds[1], "],[")

	fmt.Printf("ope = %s\n", ope)
	fmt.Printf("para = %s\n", para)

	timeStart := time.Now()

	Hash_Main(ope, para)

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
