import java.util.*;

public class OperateNestedInteger {
    public List<NestedInteger> createNestedInteger(String flds_str) {
        List<NestedInteger> ni = new ArrayList<>();
        while (flds_str.length() > 0) {
        //  System.out.println("flds_str = " + flds_str);
            if (flds_str.charAt(0) == '[') {
                int end_pos = 1, depth = 1;
                while (depth > 0 && end_pos < flds_str.length()) {
                    if (flds_str.charAt(end_pos) == '[') {
                        depth++;
                    } else if (flds_str.charAt(end_pos) == ']') {
                        depth--;
                    }
                    end_pos++;
                }
                String substr = flds_str.substring(1, end_pos - 1);
                ni.add(createListNestedInteger(substr));
                if (end_pos < flds_str.length() - 1) {
                    flds_str = flds_str.substring(end_pos + 1);
                } else {
                    flds_str = "";
                }
            } else {
                int pos1 = flds_str.indexOf(',');
                int pos2 = flds_str.indexOf(']');
                if (pos1 == -1 && pos2 == -1) {
                     ni.add(new NestedInteger(Integer.parseInt(flds_str)));
                    flds_str = "";
                } else if (pos2 >= 0) {
                    if (pos2 < pos1 || pos1 == -1) {
                        int val = Integer.parseInt(flds_str.substring(0, pos2)); 
                        ni.add(new NestedInteger(val));
                        flds_str = flds_str.substring(pos2 + 1);
                    } else {
                        int val = Integer.parseInt(flds_str.substring(0, pos1)); 
                        ni.add(new NestedInteger(val));
                        flds_str = flds_str.substring(pos1 + 1);
                    }
                } else if (pos1 >= 0) {
                    int val = Integer.parseInt(flds_str.substring(0, pos1)); 
                    ni.add(new NestedInteger(val));
                    flds_str = flds_str.substring(pos1 + 1);
                } else {
                    System.out.println("createNestedInteger() Error.");
                }
            }
        }
        return ni;
    }    

    public NestedInteger createListNestedInteger(String flds_str) {
        NestedInteger ni = new NestedInteger();
        while (flds_str.length() > 0) {
        //  System.out.println("flds_str = " + flds_str);
            while (flds_str.charAt(0) == ',') {
                flds_str = flds_str.substring(1);
            }
            if (flds_str.charAt(0) == '[') {
                int end_pos = 1, depth = 1;
                while (depth > 0 && end_pos < flds_str.length()) {
                    if (flds_str.charAt(end_pos) == '[') {
                        depth++;
                    } else if (flds_str.charAt(end_pos) == ']') {
                        depth--;
                    }
                    end_pos++;
                }
                String substr = flds_str.substring(1, end_pos - 1);
                ni.add(createListNestedInteger(substr));
                if (end_pos < flds_str.length() - 1) {
                    flds_str = flds_str.substring(end_pos + 1);
                } else {
                    flds_str = "";
                }
            } else {
                int pos1 = flds_str.indexOf(',');
                int pos2 = flds_str.indexOf(']');
                if (pos1 == -1 && pos2 == -1) {
                     ni.add(new NestedInteger(Integer.parseInt(flds_str)));
                    flds_str = "";
                } else if (pos2 >= 0) {
                    if (pos2 < pos1 || pos1 == -1) {
                        int val = Integer.parseInt(flds_str.substring(0, pos2)); 
                        ni.add(new NestedInteger(val));
                        flds_str = flds_str.substring(pos2 + 1);
                    } else {
                        int val = Integer.parseInt(flds_str.substring(0, pos1)); 
                        ni.add(new NestedInteger(val));
                        flds_str = flds_str.substring(pos1 + 1);
                    }
                } else if (pos1 >= 0) {
                    int val = Integer.parseInt(flds_str.substring(0, pos1)); 
                    ni.add(new NestedInteger(val));
                    flds_str = flds_str.substring(pos1 + 1);
                } else {
                    System.out.println("createNestedInteger() Error.");
                }
            }
        }
        return ni;
    }

    public String listNestedIntegerToString(List<NestedInteger> flds) {
        StringBuilder sb = new StringBuilder();
        for (NestedInteger ni : flds) {
            sb.append(ni.toString());
        }
        return sb.toString();
    }

    public List<Integer> getNestedIterator(List<NestedInteger> listNestedInteger) {
        List<Integer> result = new ArrayList<>();
        NestedIterator ni = new NestedIterator(listNestedInteger);
        while (ni.hasNext()) {
            result.add(ni.next());
        }
        return result;
    }
}
