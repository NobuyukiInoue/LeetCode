import java.util.*;

// Java Iterator interface reference:
// https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html

class PeekingIterator implements Iterator<Integer> {
    // 4ms
    private Integer cache = null;
    private Iterator<Integer> myIterator;

    public PeekingIterator(Iterator<Integer> iterator) {
        // initialize any member here.
        myIterator = iterator;
        if (myIterator.hasNext())
            cache = myIterator.next();
    }

    // Returns the next element in the iteration without advancing the iterator. 
    public Integer peek() {
        return cache; 
    }

    // hasNext() and next() should behave the same as in the Iterator interface.
    // Override them if needed.
    @Override
    public Integer next() {
        Integer res = cache;
        cache = myIterator.hasNext() ? myIterator.next() : null;
        return res; 
    }

    @Override
    public boolean hasNext() {
        return cache != null;
    }
}
