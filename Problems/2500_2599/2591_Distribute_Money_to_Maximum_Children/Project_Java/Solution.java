public class Solution {
    public int distMoney(int money, int children) {
        // 3ms
        money -= children;
        if (money < 0)
            return -1;
        if (money / 7 == children && money % 7 == 0)
            return children;
        if (money / 7 == children - 1 && money % 7 == 3)
            return children - 2;
        return Math.min(children - 1, money / 7);
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        int money = Integer.parseInt(flds[0]);
        int children = Integer.parseInt(flds[1]);
        System.out.println("money = " + money);
        System.out.println("children = " + children);

        long start = System.currentTimeMillis();

        int result = distMoney(money, children);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
