package main

import "fmt"

func main() {
	a := []int{1, 2, 3, 4, 5}

	fmt.Println(a[0:2]) // => "[1 2]"
	fmt.Println(a[1:4]) // => "[2 3 4]"

	// 破壊的メソッド
	num, a, _ := slice(a, 0, 2)
	fmt.Println(num) // =>"[1 2]"
	fmt.Println(a)   // =>"[3 4 5]"
	num, a, _ = slice(a, 1, 3)
	fmt.Println(num) // => "[4 5]"
	fmt.Println(a)   // => "[3]"
}

func slice(slice []int, start, end int) ([]int, []int, error) {
	if len(slice) < start || len(slice) < end {
		return nil, nil, fmt.Errorf("Error")
	}
	ans := make([]int, (end - start))
	copy(ans, slice[start:end])
	slice = append(slice[:start], slice[end:]...)
	return ans, slice, nil
}
