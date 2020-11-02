class MyCircularQueue {
    // 4ms

    private int maxlen;
    private int currlen;
    private int[] queue;
    private int head;
    private int tail; 
    /** Initialize your data structure here. Set the size of the queue to be k. */
    public MyCircularQueue(int k) {
        maxlen = k;
        currlen = 0;
        queue = new int[k];
        head = -1;
        tail = -1;
    }
    
    /** Insert an element into the circular queue. Return true if the operation is successful. */
    public boolean enQueue(int value) {
        if (isFull())
            return false;
        tail = (tail + 1) % maxlen;
        queue[tail] = value;
        currlen++;
        if (currlen == 1)
            head = 0;
        return true;
    }
    
    /** Delete an element from the circular queue. Return true if the operation is successful. */
    public boolean deQueue() {
        if (isEmpty())
            return false;
        head = (head + 1) % maxlen;
        currlen--;
        if (isEmpty()) {
            head = -1;
            tail = -1;
        }
        return true;
    }
    
    /** Get the front item from the queue. */
    public int Front() {
        if (isEmpty())
            return -1;
        return queue[head];
    }
    
    /** Get the last item from the queue. */
    public int Rear() {
        if (isEmpty())
            return -1;
        return queue[tail];
        
    }
    
    /** Checks whether the circular queue is empty or not. */
    public boolean isEmpty() {
        return (currlen == 0);
        
    }
    
    /** Checks whether the circular queue is full or not. */
    public boolean isFull() {
        return (currlen == maxlen);
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */
