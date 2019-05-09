package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func backspaceCompare(S string, T string) bool {
	slen, tlen := len(S), len(T)
	if slen == 0 && tlen == 0 {
		return true
	}
	scur, tcur := slen-1, tlen-1
	sbs, tbs := 0, 0

	for {
		for scur >= 0 && (S[scur] == '#' || sbs > 0) {
			if S[scur] == '#' {
				sbs++
			} else {
				sbs--
			}
			scur--
		}
		for tcur >= 0 && (T[tcur] == '#' || tbs > 0) {
			if T[tcur] == '#' {
				tbs++
			} else {
				tbs--
			}
			tcur--
		}

		if (scur == 0 && tcur == 0) || (scur < 0 && tcur < 0) {
			return true
		} else if (scur >= 0 && tcur < 0) || (scur < 0 && tcur >= 0) || S[scur] != T[tcur] {
			return false
		}
		scur--
		tcur--
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[[", "", -1)
	temp = strings.Replace(temp, "]]", "", -1)
	words := strings.Split(temp, "],[")
	S := words[0]
	T := words[1]

	fmt.Printf("S = %s, T = %s\n", S, T)

	timeStart := time.Now()

	result := backspaceCompare(S, T)

	timeEnd := time.Now()

	fmt.Printf("result = %s\n", strconv.FormatBool(result))
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
