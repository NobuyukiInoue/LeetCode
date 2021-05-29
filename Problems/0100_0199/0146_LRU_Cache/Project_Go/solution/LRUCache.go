package solution

import "container/list"

// 124ms

type LRUCache struct {
	capacity  int
	mapCache  map[int]*list.Element
	listCache *list.List
}

type cacheItem struct {
	key, value int
}

var defaultLRUCacheCap = 1 << 10

func Constructor(capacity int) LRUCache {
	if capacity <= 0 {
		capacity = defaultLRUCacheCap
	}
	return LRUCache{
		capacity:  capacity,
		mapCache:  make(map[int]*list.Element),
		listCache: list.New(),
	}
}

func (this *LRUCache) Get(key int) int {
	v, ok := this.mapCache[key]
	if !ok {
		return -1
	}

	this.listCache.MoveToFront(v)
	return v.Value.(*cacheItem).value
}

func (this *LRUCache) Put(key int, value int) {
	v, ok := this.mapCache[key]
	if ok {
		v.Value.(*cacheItem).value = value
		this.listCache.MoveToFront(v)
		return
	}

	if this.Len() >= this.capacity {
		this.RemoveOldest()
	}

	item := &cacheItem{key: key, value: value}
	element := this.listCache.PushFront(item)
	this.mapCache[key] = element
}

// RemoveOldest remove the oldest item of LRUCache lru.
func (lru *LRUCache) RemoveOldest() {
	element := lru.listCache.Back()
	lru.listCache.Remove(element)
	delete(lru.mapCache, element.Value.(*cacheItem).key)
}

// Len returns the length of LRUCache lru.
func (lru *LRUCache) Len() int {
	return lru.listCache.Len()
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */
