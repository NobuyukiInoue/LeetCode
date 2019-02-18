package hashset

type MyHashSet struct {
	val [100001]bool
}

/** Initialize your data structure here. */
func Constructor() MyHashSet {
	return MyHashSet{}
}

func (this *MyHashSet) Add(key int) {
	this.val[key] = true
}

func (this *MyHashSet) Remove(key int) {
	this.val[key] = false
}

/** Returns true if this set contains the specified element */
func (this *MyHashSet) Contains(key int) bool {
	return this.val[key]
}
