package solution

import (
	"fmt"
	"strings"
	"time"
)

type Stack struct {
	Val  int
	Next *Stack
}

func Constructor() Stack {
	return Stack{}
}

func (this *Stack) Push(val int) {
	nextStack := *this
	*this = Stack{val, &nextStack}
}

func (this *Stack) Pop() int {
	retVal := this.Val
	*this = *this.Next
	return retVal
}

func (this *Stack) Peek() int {
	return this.Val
}

func calculate(s string) int {
	// 8ms
	total := 0
	stack := Constructor()
	stack.Push(1)
	stack.Push(1)
	for i := 0; i < len(s); i++ {
		c := s[i]
		if c >= '0' {
			number := 0
			for i < len(s) && s[i] >= '0' {
				number = 10*number + int(s[i]-'0')
				i++
			}
			total += stack.Peek() * number
			stack.Pop()
			i--
		} else if c == ')' {
			stack.Pop()
		} else if c != ' ' {
			if c == '-' {
				stack.Push(-stack.Peek())
			} else {
				stack.Push(stack.Peek())
			}
		}
	}
	return total
}

func LoopMain(args string) {
	temp := strings.Trim(args, "")
	temp = strings.Replace(temp, "\"", "", -1)
	temp = strings.Replace(temp, "[", "", -1)
	s := strings.Replace(temp, "]", "", -1)
	fmt.Printf("s = %s\n", s)

	timeStart := time.Now()

	result := calculate(s)

	timeEnd := time.Now()

	fmt.Printf("result = %d\n", result)
	fmt.Printf("Execute time: %.3f [ms]\n\n", timeEnd.Sub(timeStart).Seconds()*1000)
}
