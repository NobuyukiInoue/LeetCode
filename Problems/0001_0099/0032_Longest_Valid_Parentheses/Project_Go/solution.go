package main

import (
	"fmt"
	"strings"
	"time"
)

/*
    public int longestValidParentheses(String s) {
        int n = s.length();
        int[] f = new int[n + 1];
        char[] c = s.toCharArray();
        int max = 0;
        for (int i = 2; i <= n; ++i) {
            if (c[i - 1] == ')') {
                if (c[i - 2] == '(') {
                    f[i] = f[i - 2] + 2;
                } else if (i - f[i - 1] - 2 >= 0 && c[i - f[i - 1] - 2] == '(') {
                    f[i] = f[i - 1] + f[i - f[i - 1] - 2] + 2;
                }
            }
            max = Math.max(max, f[i]);
        }
        return max;
	}
*/

func longestValidParentheses(s string) int {
	n := len(s)
	f := make([]int, n+1)
	maxNum := 0
	for i := 2; i <= n; i++ {
		if s[i-1] == ')' {
			if s[i-2] == '(' {
				f[i] = f[i-2] + 2
			} else if i-f[i-1]-2 >= 0 && s[i-f[i-1]-2] == '(' {
				f[i] = f[i-1] + f[i-f[i-1]-2] + 2
			}
		}
		maxNum = max(maxNum, f[i])
	}
	return maxNum
}

func max(a int, b int) int {
	if a >= b {
		return a
	} else {
		return b
	}
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, ", ", ",", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)

	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := longestValidParentheses(s)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
