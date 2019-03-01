package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func canConstruct(ransomNote string, magazine string) bool {
	alphaCount :=  [128]int{}
	for i := 0; i < len(magazine); i++ {
		alphaCount[int(magazine[i])]++
	 }

	for j := 0; j < len(ransomNote); j++ {
		alphaCount[int(ransomNote[j])]--
		if alphaCount[int(ransomNote[j])] < 0 {
			return false
		}
	}
	return true
}

func canConstruct2(ransomNote string, magazine string) bool {
	for _, sChar := range ransomNote {
		fmt.Printf("sChar = %c\n", sChar)

		//	idx := strings.Index(magazine, sChar)
		idx := -1
		tChar := '0'
		hitFlag := false

		for idx, tChar = range magazine {
			if sChar == tChar {
				fmt.Printf("idx = %d, sChar = %c, tChar = %c\n", idx, sChar, tChar)
				hitFlag = true
				break
			}
		}
		if hitFlag == false {
			return false
		}
		magazine = magazine[0:idx] + magazine[idx+1:]
	}

	return true
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)

	flds := strings.Split(temp, "],[")
	ransomNote := flds[0]
	magazine := flds[1]

	fmt.Printf("ransomeNote = %s\n", ransomNote)
	fmt.Printf("magazine = %s\n", magazine)

	timeStart := time.Now()

	result := canConstruct(ransomNote, magazine)
	fmt.Printf("result = %s\n", strconv.FormatBool(result))

	timeEnd := time.Now()

	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
