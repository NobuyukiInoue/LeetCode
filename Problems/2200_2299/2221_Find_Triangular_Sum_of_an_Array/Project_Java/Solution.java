import java.util.*;

public class Solution {
    public int triangularSum(int[] nums) {
        // 5ms
        int result = 0;
        int len = nums.length - 1;
        int mck = 1, exp2 = 0, exp5 = 0;
        int[] inv = {0, 1, 0, 7, 0, 0, 0, 3, 0, 9};
        int[] pow2mod10 = {6, 2, 4, 8};
        for (int k = 0; true; k++) {
            if (exp2 == 0 || exp5 == 0) {
                int mCk_ = exp2 > 0 ? mck * pow2mod10[exp2 % 4] : exp5 > 0 ? mck * 5 : mck;
                result = (result + mCk_ * nums[k]) % 10;
            }
            if (k == len)
                return result;

            // mCk *= m - k
            int mul = len - k;
            while (mul % 2 == 0) {
                mul /= 2;
                exp2++;
            }
            while (mul % 5 == 0) {
                mul /= 5;
                exp5++;
            }
            mck = mck * mul % 10;

            // mCk /= k + 1
            int div = k + 1;
            while (div % 2 == 0) {
                div /= 2;
                exp2--;
            }
            while (div % 5 == 0) {
                div /= 5;
                exp5--;
            }
            mck = mck * inv[div % 10] % 10;
        }
    }

    public int triangularSum_nCr(int[] nums) {
        // Wrong Anser. nCr is too Large.
        int res = 0, nCr = 1, n = nums.length - 1;
        for (int i = 0; i < nums.length; i++) {
            res = (res + nums[i]*nCr)%10;
            nCr = nCr*(n - i)/(i + 1);
        }
        return res;
    }

    public int triangularSum_while1(int[] nums) {
        // 92ms
        int n = nums.length;
        while (n != 1) {
            for (int i = 0; i < n - 1; i++) {
                nums[i] = (nums[i] + nums[i + 1])%10;
            }
            n--;
        }
        return nums[0];
    }

    public int triangularSum_while2(int[] nums) {
        // 93ms - 94ms
        while (nums.length > 1) {
            int[] temp = new int[nums.length - 1];
            for (int i = 0, j = 0; i < nums.length - 1; i++, j++) {
                temp[j] = (nums[i] + nums[i + 1])%10;
            }
            nums = temp;
        }
        return nums[0];
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = triangularSum(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
