package solution

import (
	"math/rand"
	"time"
)

// 167ms - 177ms
type RandomizedSet struct {
	Data    []int
	DataMap map[int]int
}

func Constructor() RandomizedSet {
	rand.Seed(time.Now().UnixNano())
	return RandomizedSet{make([]int, 0), make(map[int]int, 0)}
}

func (this *RandomizedSet) Insert(val int) bool {
	if _, ok := this.DataMap[val]; ok {

	} else {
		this.Data = append(this.Data, val)
		this.DataMap[val] = len(this.Data) - 1
		return true
	}
	return false
}

func (this *RandomizedSet) Remove(val int) bool {
	if index, ok := this.DataMap[val]; ok {
		delete(this.DataMap, val)
		lastVal := this.Data[len(this.Data)-1]
		this.Data = this.Data[:len(this.Data)-1]
		if lastVal != val {
			this.Data[index] = lastVal
			this.DataMap[lastVal] = index
		}
		return true
	}
	return false
}

func (this *RandomizedSet) GetRandom() int {
	return this.Data[rand.Intn(len(this.Data))]
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Insert(val);
 * param_2 := obj.Remove(val);
 * param_3 := obj.GetRandom();
 */
