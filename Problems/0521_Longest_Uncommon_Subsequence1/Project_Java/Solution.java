public class Solution {
	public int findLUSlength(String a, String b) {
		if(a.equals(b))
			return -1;
		else
			return a.length()>b.length()?a.length():b.length();
	}

    public void Main(String args) {
        System.out.println("args = " + args);
        String[] flds = args.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");
		String a = flds[0];
		String b = flds[1];

        System.out.println("a = " + a);
        System.out.println("b = " + b);

        long start = System.currentTimeMillis();

        int result = findLUSlength(a, b);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
