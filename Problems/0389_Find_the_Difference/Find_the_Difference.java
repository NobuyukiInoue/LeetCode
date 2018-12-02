import java.io.File;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.IOException;

public class Find_the_Difference {
    public static char findTheDifference(String s, String t) {
        int sum = t.charAt(0);

        for(int i = 1; i < t.length(); i++)
            sum = sum + t.charAt(i) - s.charAt(i - 1);

        return (char)sum;
    }

    public static char findTheDifference_bug(String s, String t) {
        int[] count = new int[26];
        for (char c : s.toCharArray()) {
            count[c - 'a']++;
        }
        for(char c : t.toCharArray()) {
            count[c - 'a']--;
        }        
        for (int i = 0; i < 26; i++) {
            if (count[i] != 0) return (char) (i + 97);
        }
        return ' ';
    }

    public static char findTheDifference_old(String s, String t) {
        String str = "abcdefghijklmnopqrstuvwxyz";
        String temp;

        for (int i = 0; i < str.length(); ++i) {
            temp = String.valueOf(str.charAt(i));
            if (s.split(temp).length != t.split(temp).length) {
                return str.charAt(i);
            }
        }

        return '0';
    }

    public static void main(String[] args) {
        if (args.length != 1) {
            final String className = new Object(){}.getClass().getEnclosingClass().getName();
            System.out.println("Usage:" + className + " <testdata.txt>");
            System.exit(1);
        }

        try {
            File file = new File(args[0]);

            BufferedReader br = new BufferedReader(new FileReader(file));
            String str = br.readLine();
            while(str != null){
                System.out.println(str);
                loop_main(str);
                str = br.readLine();
            }

            br.close();

        } catch(FileNotFoundException e) {
            System.out.println(e);
        } catch(IOException e) {
            System.out.println(e);
        }
    }

    public static void loop_main(String temp) {
        String[] flds = temp.split(",");
        String s = flds[0];
        String t = flds[1];

        System.out.println("s = " + s + ", t = " + t);

        long start = System.currentTimeMillis();
        
        char result = findTheDifference(s, t);
    //  char result = findTheDifference_old(s, t);

        System.out.println("result = " + result);
        
        long end = System.currentTimeMillis();
        System.out.println((end - start)  + "ms");
    }
}
