import java.util.*;

public class Solution {
    public int minNumberOfHours(int initialEnergy, int initialExperience, int[] energy, int[] experience) {
        // 1ms
        int enery_required = 0;
        int total_energy = 0;
        for (int en : energy) {
            total_energy += en;
        }

        if (total_energy >= initialEnergy) {
            enery_required = total_energy - initialEnergy + 1;
        }

        int exp_required = 0;
        for (int exp : experience) {
            int training_exp = 0;
            if (initialExperience <= exp) {
                training_exp = exp - initialExperience + 1;
                exp_required += training_exp;
            }
            initialExperience += exp + training_exp;
        }
        return enery_required + exp_required;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int initialEnergy = Integer.parseInt(flds[0]);
        int initialExperience = Integer.parseInt(flds[1]);
        int[] energy = ml.stringToIntArray(flds[2]);
        int[] experience = ml.stringToIntArray(flds[3]);

        System.out.println("initialEnergy = " + Integer.toString(initialEnergy)
                    + ", initialExperience = " + Integer.toString(initialExperience)
                    + ", energy = " + ml.intArrayToString(energy)
                    + ", experience = " + ml.intArrayToString(experience));

        long start = System.currentTimeMillis();

        int result = minNumberOfHours(initialEnergy, initialExperience, energy, experience);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
