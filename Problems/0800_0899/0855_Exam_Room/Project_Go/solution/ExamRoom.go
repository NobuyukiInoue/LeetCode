package solution

// 139ms - 143ms

type ExamRoom struct {
	N      int
	indexs []int
}

func Constructor(N int) ExamRoom {
	return ExamRoom{N, make([]int, 0)}
}

func (this *ExamRoom) Seat() int {
	if len((*this).indexs) == 0 {
		(*this).indexs = append((*this).indexs, 0)
		return 0
	}
	d := myMax((*this).indexs[0], (*this).N-1-(*this).indexs[len((*this).indexs)-1])
	for i := 0; i < len((*this).indexs)-1; i++ {
		d = myMax(d, ((*this).indexs[i+1]-(*this).indexs[i])/2)
	}
	if (*this).indexs[0] == d {
		(*this).indexs = append([]int{0}, (*this).indexs...)
		return 0
	}
	for i := 0; i < len((*this).indexs)-1; i++ {
		if ((*this).indexs[i+1]-(*this).indexs[i])/2 == d {
			(*this).indexs = append((*this).indexs[:i+1], append([]int{((*this).indexs[i+1] + (*this).indexs[i]) / 2}, (*this).indexs[i+1:]...)...)
			return (*this).indexs[i+1]
		}
	}
	(*this).indexs = append((*this).indexs, (*this).N-1)
	return (*this).N - 1
}

func (this *ExamRoom) Leave(p int) {
	for i := 0; i < len((*this).indexs); i++ {
		if (*this).indexs[i] == p {
			(*this).indexs = append((*this).indexs[:i], (*this).indexs[i+1:]...)
		}
	}
}

func myMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}

/**
 * Your ExamRoom object will be instantiated and called as such:
 * obj := Constructor(N);
 * param_1 := obj.Seat();
 * obj.Leave(p);
 */
