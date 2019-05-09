import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class Solution {
    public int total = 0;
    public int getImportance2(List<Employee> employees, int id) {
        Employee manager = employees.stream().filter(e -> e.id == id).collect(Collectors.toList()).get(0);
        total += manager.importance;
        manager.subordinates.forEach(subId -> getImportance2(employees, subId));
        return total;
    }

    public int result = 0;
    public int getImportance(List<Employee> employees, int id) {
        Map<Integer, Employee> map = new HashMap<>();
        for(Employee employee : employees) {
            map.put(employee.id, employee);
        }
        this.dfs(map.get(id), map);
        return result;
    }
    
    private void dfs(Employee employee, Map<Integer, Employee> map) {
        if(employee == null) {
            return;
        }
        result += employee.importance;
        for(Integer id : employee.subordinates) {
            dfs(map.get(id), map);
        }
    }

    public Employee set_Employee(String data) {
        String[] flds = data.split(",\\[");
        String[] id_and_importance = flds[0].split(",");
        int id = Integer.parseInt(id_and_importance[0]);
        int importance = Integer.parseInt(id_and_importance[1]);

        List<Integer> subordinates = new ArrayList<Integer>();

        if (flds.length > 1) {
            String[] subordinates_str = flds[1].split(",");

            for (int i = 0; i < subordinates_str.length; i++ ) {
                subordinates.add(Integer.parseInt(subordinates_str[i]));
            }
        }

        Employee em = new Employee(id, importance, subordinates);

        return em;
    }

    public String employee2String(Employee em) {
        String resultStr = Integer.toString(em.id) + ", " + Integer.toString(em.importance) + ", [";
        for (int i = 0; i < em.subordinates.size(); i++ ) {
            if (i == 0)
                resultStr += em.subordinates.get(i);
            else
                resultStr += ", " + em.subordinates.get(i);
        }

        return resultStr + "]";
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        int pos_id = args.lastIndexOf(",");
        int id = Integer.parseInt(args.substring(pos_id + 1).replace(" ", "").replace("]", "").trim());
        String[] flds = args.substring(0, pos_id).replace(" ", "").replace("[[[", "").replace("]]]", "").split("\\]\\],\\[");

        List<Employee> employees = new ArrayList<Employee>();
    
        for (int i = 0; i < flds.length; i++ ) {
            employees.add(set_Employee(flds[i]));
            System.out.println("employees[" + Integer.toString(i) + "] = " + employee2String(employees.get(i)));
        }

        System.out.println("id = " + Integer.toString(id));

        long start = System.currentTimeMillis();

        total = 0;
        result = 0;
        int result = getImportance(employees, id);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
