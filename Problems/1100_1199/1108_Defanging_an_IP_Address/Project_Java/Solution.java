import java.util.*;

public class Solution {
    public String defangIPaddr(String address) {
        return address.replace(".", "[.]");
    }

    public String Int_array_to_String(int[] data) {
        String result = "";
    
        for (int i = 0; i < data.length; i++) {
            if (i > 0)
                result += ",";

            if (data[i] == -1)
                result += "null";
            else
                result += Integer.toString(data[i]);
        }
    
        return result;
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
