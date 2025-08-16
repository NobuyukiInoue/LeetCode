import java.util.*;

public class Solution {
    public List<String> validateCoupons(String[] code, String[] businessLine, boolean[] isActive) {
        // 9ms
        List<String> result = new ArrayList<>();
        Set<String> validBusinessLines = new HashSet<>(Arrays.asList(
            "electronics", "grocery", "pharmacy", "restaurant"
        ));
        List<String[]> validCoupons = new ArrayList<>();

        for (int i = 0; i < code.length; i++) {
            if (isValid(code[i], isActive[i], businessLine[i], validBusinessLines)) {
                validCoupons.add(new String[]{code[i], businessLine[i]});
            }
        }

        String[] order = {"electronics", "grocery", "pharmacy", "restaurant"};
        for (String category : order) {
            List<String> temp = new ArrayList<>();
            for (String[] pair : validCoupons) {
                if (pair[1].equals(category)) {
                    temp.add(pair[0]);
                }
            }
            Collections.sort(temp);
            result.addAll(temp);
        }

        return result;
    }

    boolean isValid(String code, boolean isActive, String businessLine, Set<String> validBusinessLines) {
        if (code == null || code.length() == 0) return false;

        for (int i = 0; i < code.length(); i++) {
            char c = code.charAt(i);
            if (!Character.isLetterOrDigit(c) && c != '_') {
                return false;
            }
        }

        if (!validBusinessLines.contains(businessLine))
            return false;
        if (!isActive)
            return false;
        return true;
    }

    private boolean[] stringArrayToBoolArray(String[] flds) {
        boolean[] res = new boolean[flds.length];
        for (int i = 0; i < flds.length; i++) {
            if (flds[i].equals("true")) {
                res[i] = true;
            } else {
                res[i] = false;
            }
        }
        return res;
    }

    private String booleanArrayToString(boolean[] flds) {
        if (flds == null)
            return "[]";
        if (flds.length <= 0)
            return "[]";

        StringBuilder resultStr = new StringBuilder("[" + Boolean.toString(flds[0]));
        for (int i = 1; i < flds.length; ++i)
            resultStr.append("," + Boolean.toString(flds[i]));
        resultStr.append("]");

        return resultStr.toString();
    }

    public void Main(String temp) {
        String flds[] = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        String[] code = flds[0].split(",");
        String[] businessLine = flds[1].split(",");
        boolean[] isActive = stringArrayToBoolArray(flds[2].split(","));

        Mylib ml = new Mylib();
        System.out.println("code = " + ml.stringArrayToString(code) + ", bisinessLine = " + ml.stringArrayToString(businessLine) + ", isActive = " + booleanArrayToString(isActive));

        long start = System.currentTimeMillis();

        List<String> result = validateCoupons(code, businessLine, isActive);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
