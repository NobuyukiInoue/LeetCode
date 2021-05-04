package solution

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func solveEquation(equation string) string {
	// 0ms
	flds := strings.Split(equation, "=")
	lx, ln := helper(flds[0])
	rx, rn := helper(flds[1])
	x := lx - rx
	n := rn - ln
	if x == 0 {
		if n == 0 {
			return "Infinite solutions"
		}
		return "No solution"
	}
	return "x=" + strconv.Itoa(n/x)
}

func helper(s string) (int, int) {
	sign, n := 1, len(s)
	coefficient, number := 0, 0
	i := 0
	for i < n {
		if s[i] == '+' {
			sign = 1
		} else if s[i] == '-' {
			sign = -1
		} else if isDigit(s[i]) {
			j := i
			for j < n && isDigit(s[j]) {
				j++
			}
			tmp, _ := strconv.Atoi(s[i:j])
			if j < n && s[j] == 'x' {
				coefficient += tmp * sign
				j++
			} else {
				number += tmp * sign
			}
			i = j - 1
		} else {
			coefficient += 1 * sign
		}
		i++
	}
	return coefficient, number
}

func isDigit(ch byte) bool {
	if '0' <= ch && ch <= '9' {
		return true
	}
	return false
}

/*
func helper2(equation string) (int, int) {
	equation += "+" // to simplify the code
	sign := 1
	current := ""
	coefficient, number := 0, 0
	for _, v := range equation {
		switch v {
		case '+':
			n, _ := strconv.Atoi(current)
			number += sign * n
			sign = 1
			current = ""
		case '-':
			n, _ := strconv.Atoi(current)
			number += sign * n
			sign = -1
			current = ""
		case 'x':
            // if current is empty, set it "1"
            if current == "" {
                current = "1"
            }
			n, _ := strconv.Atoi(current)
			coefficient += sign * n
			current = "0"
		default:
			current += string(v)
		}
	}
	return coefficient, number
}
*/

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	equation := strings.Replace(temp, "]", "", -1)
	fmt.Printf("equation = %s\n", equation)

	timeStart := time.Now()

	result := solveEquation(equation)

	timeEnd := time.Now()

	fmt.Printf("result = \"%s\"\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
