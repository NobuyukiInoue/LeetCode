import java.util.*;

// 2ms - 7ms
public class NestedIterator implements Iterator<Integer> {
    private List<Integer> integerList = new ArrayList<>();
    private int index = 0;

    public NestedIterator(List<NestedInteger> nestedList) {
        for (NestedInteger nestedInteger : nestedList) {
            flatten(nestedInteger);
        }
    }

    private void flatten(NestedInteger nested) {
        if (nested.isInteger()) {
            integerList.add(nested.getInteger());
        } else {
            for (NestedInteger nestedFromList : nested.getList()) {
                flatten(nestedFromList);
            }
        }
    }

    @Override
    public Integer next() {
        return integerList.get(index++);
    }

    @Override
    public boolean hasNext() {
        return index < integerList.size();
    }
}

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i = new NestedIterator(nestedList);
 * while (i.hasNext()) v[f()] = i.next();
 */
