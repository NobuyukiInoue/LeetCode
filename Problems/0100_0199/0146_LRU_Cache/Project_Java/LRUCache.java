import java.util.*;

public class LRUCache extends LinkedHashMap<Integer, Integer> {
    // 12ms
    private int capacity;

    public LRUCache(int capacity) {
        super(capacity, 0.75f, true);
        this.capacity = capacity;
    }

    @Override
    protected boolean removeEldestEntry(Map.Entry<Integer, Integer> eldest) {
        return size() > capacity;
    }

    public int get(int key) {
        return getOrDefault(key, -1);
    }

    public void put(int key, int value) {
        super.put(key, value);
    }
}

/*
class LRUCache {
    // 15ms
    private Map<Integer, Integer> map = new LinkedHashMap<Integer, Integer>();
    private int capacity;

    public LRUCache(int capacity) {
        this.capacity = capacity;
    }

    public int get(int key) {
        if (!map.containsKey(key))
            return -1;
        int val;
        val = map.get(key);
        put(key, val);
        return val;
    }

    public void put(int key, int value) {
        if (!map.containsKey(key) && (map.size() == capacity)) {
            map.remove(map.keySet().iterator().next());
        }
        map.remove(key);
        map.put(key, value);
    }
}
*/

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
