import java.util.*;

class ExamRoom {
    // 467ms - 1282ms
    int N;
    ArrayList<Integer> indexs = new ArrayList<>();

    public ExamRoom(int n) {
        N = n;
    }

    public int seat() {
        if (indexs.size() == 0) {
            indexs.add(0);
            return 0;
        }
        int d = Math.max(indexs.get(0), N - 1 - indexs.get(indexs.size() - 1));
        for (int i = 0; i < indexs.size() - 1; i++) {
            d = Math.max(d, (indexs.get(i + 1) - indexs.get(i)) / 2);
        }
        if (indexs.get(0) == d) {
            indexs.add(0, 0);
            return 0;
        }
        for (int i = 0; i < indexs.size() - 1; i++) {
            if ((indexs.get(i + 1) - indexs.get(i)) / 2 == d) {
                indexs.add(i + 1, (indexs.get(i + 1) + indexs.get(i)) / 2);
                return indexs.get(i + 1);
            }
        }
        indexs.add(N - 1);
        return N - 1;
    }

    public void leave(int p) {
        for (int i = 0; i < indexs.size(); i++) {
            if (indexs.get(i) == p) {
                indexs.remove(i);
            }
        }
    }
}

/**
 * Your ExamRoom object will be instantiated and called as such:
 * ExamRoom obj = new ExamRoom(n);
 * int param_1 = obj.seat();
 * obj.leave(p);
 */
