import java.util.*;

public class Solution {
    public String defangIPaddr(String address) {
        return address.replace(".", "[.]");
    }

    public void Main(String temp) {
        String address = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        System.out.println("address = " + address);

        long start = System.currentTimeMillis();

        String result = defangIPaddr(address);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
