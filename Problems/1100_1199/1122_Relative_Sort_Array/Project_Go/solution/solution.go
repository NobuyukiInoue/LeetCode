package solution

import (
	"fmt"
	"strings"
	"time"
)

func relativeSortArray(arr1 []int, arr2 []int) []int {
	tempMap := map[int]int{}
	a := []int{}
	b := []int{}
	temp := []int{}

	for _, v := range arr1 {
		tempMap[v]++
	}
	for _, v := range arr2 {
		for I := 0; I < tempMap[v]; I++ {
			a = append(a, v)
		}
		delete(tempMap, v)
	}
	for key, value := range tempMap {
		for I := 0; I < value; I++ {
			temp = append(temp, key)
		}
	}
	length := len(temp)
	for i := 0; i < length; i++ {
		n := temp[0]
		index := 0
		for I, V := range temp {
			if n > V {
				n = V
				index = I
			}
		}
		temp = append(temp[:index], temp[index+1:]...)
		b = append(b, n)
	}

	a = append(a, b...)

	return a
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, " ", "", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	flds := strings.Split(temp, "],[")

	arr1 := StringToIntArray(flds[0])
	arr2 := StringToIntArray(flds[1])

	fmt.Printf("arr1 = [%s], arr2 = [%s]\n", IntArrayToString(arr1), IntArrayToString(arr2))

	timeStart := time.Now()

	result := relativeSortArray(arr1, arr2)

	timeEnd := time.Now()

	fmt.Printf("result = [%s]\n", IntArrayToString(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
