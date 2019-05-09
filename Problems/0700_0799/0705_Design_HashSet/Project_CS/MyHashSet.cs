public class MyHashSet
{
    private bool[] val;

    /** Initialize your data structure here. */
    public MyHashSet()
    {
        val = new bool[100001];
    }
    
    public void Add(int key)
    {
        val[key] = true;    
    }
    
    public void Remove(int key)
    {
        val[key] = false;
    }
    
    /** Returns true if this set contains the specified element */
    public bool Contains(int key)
    {
        return val[key];
    }

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.Add(key);
 * obj.Remove(key);
 * bool param_3 = obj.Contains(key);
 */
}
