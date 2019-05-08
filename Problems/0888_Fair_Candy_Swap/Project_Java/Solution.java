import java.util.*;
import java.util.stream.IntStream;

public class Solution {
    public int[] fairCandySwap(int[] A, int[] B) {
        // 15ms
        int[] swap = new int[2];
		int aSum = 0, bSum = 0;
		Set<Integer> bSet = new HashSet<Integer>();
		for (int i = 0; i < A.length; i++)
			aSum += A[i];
		for (int j = 0; j < B.length; j++) {
			bSum += B[j];
			bSet.add(B[j]);
		}
		int diff = Math.abs(aSum - bSum) / 2;
		for (int i = 0; i < A.length; i++) {
			if (aSum < bSum && bSet.contains(A[i] + diff)) {
				swap[0] = A[i];
				swap[1] = A[i] + diff;
				break;
			}
			if (aSum > bSum && bSet.contains(A[i] - diff)) {
				swap[0] = A[i];
				swap[1] = A[i] - diff;
				break;
			}
		}
		return swap;
    }

    public int[] fairCandySwap2(int[] A, int[] B) {
        // 36ms
        int dif = (IntStream.of(A).sum() - IntStream.of(B).sum()) / 2;
        HashSet<Integer> S = new HashSet<>();
        for (int a : A)
            S.add(a);
        for (int b : B)
            if (S.contains(b + dif))
                return new int[] {b + dif, b};
        return new int[0];
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();

        String[] data;
        
        int[] A = ml.str_to_int_array(flds[0]);
        int[] B = ml.str_to_int_array(flds[1]);

        System.out.println("A = " + ml.output_int_array(A));
        System.out.println("B = " + ml.output_int_array(B));
    
        long start = System.currentTimeMillis();
        
        int[] result = fairCandySwap(A, B);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.output_int_array(result));
        System.out.println((end - start)  + "ms\n");
    }
}
