/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return empty list if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */

import java.util.*;

public class NestedInteger {
    private Integer val;
    private List<NestedInteger> list;

    public NestedInteger(Integer integer){
        this.val = integer;
    }

    public NestedInteger(List<NestedInteger> list){
        this.list = list;
    }
    
    public void add(NestedInteger nestedInteger) {
        if (this.list != null) {
            this.list.add(nestedInteger);
        } else {
            this.list = new ArrayList<>();
            this.list.add(nestedInteger);
        }
    }

    public void setInteger(int num) {
        this.val = num;
    }

    public NestedInteger() {
        this.list = new ArrayList<>();
    }

    public boolean isInteger() {
        return this.val != null;
    }

    public Integer getInteger() {
        return this.val;
    }

    public List<NestedInteger> getList() {
        return list;
    }
    
    public String toString() {
        StringBuilder sb = new StringBuilder();
        if (this.isInteger()) {
            sb.append(this.val);
        }
        if (this.list != null) {
            if (sb.length() > 0) {
                sb.append(",");
            }
            sb.append("[");
            for (NestedInteger ni : this.list) {
                if (this.isInteger()) {
                    if (sb.charAt(sb.length() - 1) != '[') {
                        sb.append("," + ni.val);
                    } else {
                        sb.append(ni.val);
                    }
                } else {
                    if (sb.charAt(sb.length() - 1) != '[') {
                        sb.append("," + ni.toString());
                    } else {
                        sb.append(ni.toString());
                    }
                }
            }
            sb.append("]");
        }
        return sb.toString();
    }
}
