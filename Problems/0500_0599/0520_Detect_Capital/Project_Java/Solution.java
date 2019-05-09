public class Solution {
    public boolean detectCapitalUse(String word) {
		String left = word.substring(1);
		if (Character.isLowerCase(word.charAt(0))) {
			return !isNotAllLower(left);
		} else {
			return !(isNotAllLower(left) && isNotAllUpper(left));
		}
	}

	public boolean isNotAllLower(String str) {
		for (int i = 0; i < str.length(); ++i) {
			if (Character.isUpperCase(str.charAt(i)))
				return true;
		}
		return false;
	}

	public boolean isNotAllUpper(String str) {
		for (int i = 0; i < str.length(); ++i) {
			if (Character.isLowerCase(str.charAt(i)))
				return true;
		}
		return false;
    }

    public boolean detectCapitalUse2(String word) {
        return word.matches("[A-Z]+|[a-z]+|[A-Z][a-z]+");
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String word = args.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        System.out.println("word = " + word);

        long start = System.currentTimeMillis();

        boolean result = detectCapitalUse(word);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
