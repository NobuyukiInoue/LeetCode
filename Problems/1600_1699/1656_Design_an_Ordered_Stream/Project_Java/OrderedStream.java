import java.util.*;

class OrderedStream {
    // 66ms

    String[] stream;
    int currentIndex = 0;

    public OrderedStream(int n) {
        stream = new String[n];
    }

    public List<String> insert(int id, String value) {
        stream[id - 1] = value;
        List<String> res = new ArrayList<>();

        while (currentIndex < stream.length) {
            if (stream[currentIndex] != null) {
                res.add(stream[currentIndex++]);
            } else {
                break;
            }
        }

        return res;
    }
}

/*
class OrderedStream {
    // 68ms

    String[] stream;
    int currentIndex;

    public OrderedStream(int n) {
        stream = new String[n];
        currentIndex = 0;
    }

    public List<String> insert(int id, String value) {
        stream[id - 1] = value;
        int i;
        List<String> res = new ArrayList<>();
        for (i = currentIndex; i < stream.length; i++) {
            if (stream[i] == null)
                break;
            res.add(stream[i]);
        }
        currentIndex = i;

        return res;
    }
}
*/

/**
 * Your OrderedStream object will be instantiated and called as such:
 * OrderedStream obj = new OrderedStream(n);
 * List<String> param_1 = obj.insert(id,value);
 */
 